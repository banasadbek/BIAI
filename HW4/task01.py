list = input('enter the list')
item = input('enter the item')
count= 0
for index in list:
    if index == item:
        count +=1
print(count)