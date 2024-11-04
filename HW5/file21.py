num_letters_per_line = 5 
file = open('alphabet.txt', 'w')
for i in range(ord('A'), ord('Z') + 1):
    file.write(chr(i))
    if (i - ord('A') + 1) % num_letters_per_line == 0:
        file.write('\n')
file.close()
print("Alphabet written to alphabet.txt with", num_letters_per_line, "letters per line.")