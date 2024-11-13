a = list(map(str, input('Enter the initial list: ').split()))
b = a.copy()
b.reverse()
for index in b:
    print(index, end=' ')