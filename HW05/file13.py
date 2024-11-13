a = 'filename.txt'
b = 'copy.txt'
file = open(a, 'r')
content = file.read()
file.close()
file = open(b, 'w')
file.write(content)
file.close()