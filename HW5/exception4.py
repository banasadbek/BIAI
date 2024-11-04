try:
    number1 = float(input('Enter a float number: '))
    number2 = float(input('Enter a float number: '))
    print(number1+number2)
except TypeError:
    print('Enter the correct inputs.')