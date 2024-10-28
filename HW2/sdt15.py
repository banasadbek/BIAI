sentence = input('enter the sentence: ')
even_numbers = []
size = len(sentence)
number = 0
while number+2 < size:
    even_numbers.append(number)
    number+=2
for index in even_numbers:
    print(sentence[index], end='')