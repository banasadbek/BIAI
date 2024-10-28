number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))
number3 = float(input('Enter the third number: '))
numbers = []
numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
print(f'largest is {max(numbers)}, the smallest is {min(numbers)}')