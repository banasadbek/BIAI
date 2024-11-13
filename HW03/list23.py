a = list(map(int, input('Enter the initial list: ').split()))
odd_numbers = []
for index in a:
    if index % 2==1:
        odd_numbers.append(index)
print(odd_numbers)