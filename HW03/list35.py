a, b = map(int, input('Enter the stating and ending number: ').split())
mylist = []
for index in range(a,b+1):
    mylist.append(index)
print(mylist)