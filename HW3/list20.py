a = list(map(int, input('Enter the initial list: ').split()))
largest = max(a)
print(largest)
second = 0
for index in a:
    if index> second and largest>index:
        second = index
    
print(second)