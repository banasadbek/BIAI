try:
    number = int(input('Enter an integer: '))
    print(number)
except ValueError:
    print('Enter valid integer')