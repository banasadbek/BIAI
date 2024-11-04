a = list(map(int, input('Enter the initial list: ').split()))
smallest = min(a)
print(smallest)
second = 100000
for index in a:
    if index < second and smallest<index:
        second = index
    
print(second)