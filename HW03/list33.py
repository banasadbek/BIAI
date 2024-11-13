a = list(map(int, input('Enter the initial list: ').split()))
item = int(input('Enter the item: '))
for index in range(len(a)):
    if a[index] == item:
        print(index)