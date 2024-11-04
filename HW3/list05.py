a = list(input('Enter the list: ').split(','))
item = input('Enter the list item to search: ')
for index in a:
    if index == item:
        print(f'{item} is present in the list')
        break
print(a)