text_to_append = "This is a new line."
file = open('filename.txt', 'a')
file.write(text_to_append + '\n')
file.close()
file = open('filename.txt', 'r')
updated_content = file.read()
file.close()
print(updated_content)