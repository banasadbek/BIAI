import os
import pandas as pd
import pyodbc
from datetime import datetime


SERVER_NAME = '.'
DATABASE_NAME = 'NewDatabase'
FOLDER_PATH = 'source_files'
LOG_FILE = 'logs\\log.txt'

def log_write(message : str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"[{timestamp}] {message}\n"

    with open(LOG_FILE, 'a') as log_file:
        log_file.write(msg)
    
    print(msg[:-1])

def exists(server : str, database : str):
    with pyodbc.connect(
                        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                        f"SERVER={server};"
                        f"Trusted_Connection=yes;"
                        f"DATABASE={database};"
                    ) as connection:
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT name FROM sys.databases WHERE name = '{database}'")
            db_exists = cursor.fetchone()

            if not db_exists:
                log_write(f"Database '{database}' does not exist. Creating it...")
                cursor.execute(f"CREATE DATABASE [{database}]")
                log_write(f"Database '{database}' created successfully.")
            else:
                log_write(f"Database '{database}' already exists.")

def csv_to_sql(file_path, table_name, connection):
    df = pd.read_csv(file_path)

    for col_name, dtype in zip(df.columns, df.dtypes):
        if dtype == 'float64' or dtype == 'object':
            df[col_name] = pd.to_numeric(df[col_name], errors='coerce')

    df = df.fillna(0.0)

    cursor = connection.cursor()

    cursor.execute(f"""
                        IF OBJECT_ID('{table_name}', 'U') IS NOT NULL 
                        DROP TABLE {table_name}
                    """)
    connection.commit()

    query = f"CREATE TABLE {table_name} ("
    
    for col_name, dtype in zip(df.columns, df.dtypes):
        if dtype == 'int64':
            sql_type = 'INT'
        elif dtype == 'float64':
            sql_type = 'FLOAT'
        elif dtype == 'bool':
            sql_type = 'BIT'
        else:
            sql_type = 'VARCHAR(MAX)'
        query += f"[{col_name}] {sql_type}, "
        
    query = query[:-2] + ')'

    cursor.execute(query)
    connection.commit()

    for row in df.itertuples(index=False):
        placeholders = ', '.join(['?'] * len(row))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        try:
            cursor.execute(insert_query, *row)
        except Exception as e:
            log_write(f"Error inserting row: {row}")
            log_write(f"Error details: {e}")
    
    connection.commit()
    cursor.close()

def main():
    log_write("Processing files has started")
    
    exists(SERVER_NAME, DATABASE_NAME)
    
    connection = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SERVER_NAME};"
        f"Trusted_Connection=yes;"
        f"DATABASE={DATABASE_NAME};"
    )
    
    try:
        for file in os.listdir(FOLDER_PATH):
            if file.endswith('.csv'):
                file_path = os.path.join(FOLDER_PATH, file)
                table_name = f"{DATABASE_NAME}.dbo.{os.path.splitext(file)[0]}"
                log_write(f"Processing {file} into table {table_name}...")
                csv_to_sql(file_path, table_name, connection)
                log_write(f"Table {table_name} created successfully.")
    except Exception as e:
        log_write(f"An error occurred: {e}")
    finally:
        connection.close()
        log_write("Processing files has finished")

main()