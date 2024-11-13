email = input('enter email: ')
size = len(email)
count = -1
for index in email:
    count +=1
    if index == '@':
        position = count
print(email[:position])