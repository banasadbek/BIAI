a = list(map(int, input('Enter the initial list: ').split()))
sum = 0
for index in a:
    if index<0:
        sum+=index
print(sum)