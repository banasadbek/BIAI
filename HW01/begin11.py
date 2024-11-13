a = 0
b = 0
while a==0 or b==0:
    print('Enter a value not zero')
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
multiply = a*b
addition = a+b
def find_module(a):
    if a < 0:
        return a*(-1)
    else:
        return a
moda = find_module(a), 
modb = find_module(b)
print('multiple, addition, module of a and b are', multiply, addition, moda, modb)

