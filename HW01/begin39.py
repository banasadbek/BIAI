A = float(input('enter a: '))
B = float(input('enter b: '))
C = float(input('enter c: '))
d = B**2 - 4*A*C
if d>0:
    x1 = (-B+d**(1/2))/(2*A)
    x2 = (-B-d**(1/2))/(2*A)
    print(f'x1 = {x1}, x2 = {x2}')
else:
    print('d <= 0')