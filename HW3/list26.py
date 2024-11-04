a = list(map(int, input('Enter the initial list: ').split()))
size = len(a)
if size%2:
    print(a[(size//2)])
else:
    print(a[size//2-1], a[(size//2)])
