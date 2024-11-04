a = list(map(str, input('Enter the initial list: ').split()))
count = 0
for index in a:
    if int(index)%2 ==0:
        count+=1
print(count)