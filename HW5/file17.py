file = open('filename.txt', 'r')
lines = file.readlines()
file.close()
lines_without_newline = [line.replace('\n', '') for line in lines]
with open('filename_without_newline.txt', 'w') as output_file:
    for line in lines_without_newline:
        output_file.write(line)
print("Newline characters removed and written to filename_without_newline.txt.")