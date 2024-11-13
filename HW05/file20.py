for char in range(ord('A'), ord('Z') + 1):
    filename = f'{chr(char)}.txt'
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}.\n")
