try:
    number1 = float(input('Enter the first number: '))
    number2 = float(input('Enter the second number: '))
    sum = number1/number2
    print(sum)
except ArithmeticError:
    print('Arithmetic Error has occured')