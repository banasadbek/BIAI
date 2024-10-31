number = int(input('Enter a positive integer: '))

for index in range(1, number+1):
    if number%index==0:
        print(f'{index} is a factor of {number}')

