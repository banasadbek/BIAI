a = list(map(str, input('Enter the initial list: ').split()))
item = input('Enter the item to replace: ')
newitem = input('Enter the replace element: ')
for index in range(len(a)-1):
    if a[index] == item:
        a[index] = newitem
        break

print(a)