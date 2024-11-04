num = 5 
file = open('alphabet.txt', 'w')
for i in range(ord('A'), ord('Z') + 1):
    file.write(chr(i))
    if (i - ord('A') + 1) % num == 0:
        file.write('\n')
file.close()