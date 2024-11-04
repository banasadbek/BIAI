file = open('filename.txt', 'r')
a = []
for line in file:
    a.append(line.strip())
file.close()

b = list(set(a))
a.sort()
b.sort()

for i in b:
    print("Frequency of {} is {}".format(i,a.count(i)))