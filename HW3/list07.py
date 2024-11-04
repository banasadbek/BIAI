a = list(map(str, input('Enter the list: ').split()))
size = len(a)
print(a)
if size == 0:
    print('List is empty')
else:
    print(a[size-1])