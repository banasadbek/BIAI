number1 = int(input('enter the first number: '))
number2 = int(input('enter the second number: '))
number3 = int(input('enter the third number: '))
if number1 != number2 and number2 != number3:
    print(True, 'all three numbers are different')
else:
    print(False, 'some numbers are similar')