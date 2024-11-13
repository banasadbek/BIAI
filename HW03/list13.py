a = list(map(str, input('Enter the initial list: ').split()))
item = input('Enter the element: ')
for index in range(len(a)):
    if a[index] == item:
        print(index)
        break