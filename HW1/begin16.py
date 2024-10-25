x1 = float(input("Enter a value: "))
x2 = float(input("Enter another value: "))

distance = x1-x2
if distance < 0:
    distance *= (-1)
print("Distance between them is", distance)