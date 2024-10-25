a = -1
b = -1
while a<=0 or b<=0:
    print('Enter a value not zero')
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
c = (a**2+b**2)**(1/2)
P = a+b+c
print('C is', c, '\nParameter of triangle is', P)