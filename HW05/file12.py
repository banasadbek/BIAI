list_to_write = ['a', 'b', 'c']
file = open('output.txt', 'w')
for item in list_to_write:
    file.write(item + '\n')
file.close()