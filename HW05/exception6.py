try:
    a = list(map(int, input('Enter a list of integers: ').split()))
    for index in range(20):
        print(a[index])
except IndexError:
    print('Index out of range')