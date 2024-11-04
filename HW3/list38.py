a = list(map(int, input('Enter the initial list: ').split()))
b = a.copy()
b.reverse()
if a == b:
    print(True)
else:
    print(False)