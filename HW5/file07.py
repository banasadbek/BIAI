file = open('filename.txt', 'r')
lines_array = []
for line in file:
    lines_array.append(line.strip())
file.close()
print(lines_array)