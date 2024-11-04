extracted_chars = []
for char in range(ord('A'), ord('C')):
    filename = f'{chr(char)}.txt'  
    try:
        file = open(filename, 'r')
        content = file.read()
        extracted_chars.extend(content) 
        file.close()
    except FileNotFoundError:
        print(f"{filename} not found.")
print("Extracted characters:", extracted_chars)