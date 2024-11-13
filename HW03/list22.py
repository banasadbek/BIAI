a = list(map(int, input('Enter the initial list: ').split()))
even_numbers = []
for index in a:
    if index % 2==0:
        even_numbers.append(index)
print(even_numbers)