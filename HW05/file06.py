file = open('filename.txt', 'r')
lines_variable = ''
for line in file:
    lines_variable += line
file.close()
print(lines_variable)