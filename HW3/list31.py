a = list(map(int, input('Enter the initial list: ').split()))
number = int(input('Enter the number of repeats: '))
for index in a:
    for i in range(number):
        print(index, end=' ')