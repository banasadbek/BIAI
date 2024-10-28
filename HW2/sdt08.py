sentence = input('Enter sentence: ')
words = sentence.split()
print(words)
for index in words:
    print(index.capitalize(), end= ' ')