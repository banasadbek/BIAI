file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')
a = []
lines1 = file1.readlines()
lines2 = file2.readlines()
for line1, line2 in zip(lines1, lines2):
    a.append(line1.strip() + ' ' + line2.strip())
file1.close()
file2.close()

with open('combined.txt', 'w') as output_file:
    for line in a:
        output_file.write(line + '\n')
print("Combined lines written to combined.txt.")