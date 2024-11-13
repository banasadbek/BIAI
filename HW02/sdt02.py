sentence = input('Enter the sentence: ')
wovels = ['a','e','u','o','i']
for index in wovels:
    sentence = sentence.replace(index, '')
print(sentence)
