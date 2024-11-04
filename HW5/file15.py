import random
file = open('filename.txt', 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]
print(lines)
rn = random.choice(lines).strip()
file.close()
print("Random line:", rn)