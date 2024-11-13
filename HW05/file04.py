n = 5
file = open('filename.txt', 'r')
lines = file.readlines()
last_n_lines = lines[-n:]
file.close()
for line in last_n_lines:
    print(line.strip())