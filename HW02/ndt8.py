number1, number2 = map(str, input('Enter two values: ').split())
temp = number2
number2 = number1
number1 = temp
print(number1, number2)
