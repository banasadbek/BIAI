file = open('filename.txt', 'r')
lines_list = []
for line in file:
    lines_list.append(line.strip())
file.close()
print(lines_list)