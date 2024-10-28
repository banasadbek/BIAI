sentence = input('Enter the sentence: ')
reverse = reversed(sentence)
reverse2 = ''
for index in reverse:
    reverse2 = reverse2 + index
if reverse2 == sentence:
    print('palindrome')
else:
    print('not palindrome')