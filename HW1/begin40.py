A1 = float(input('enter a: '))
B1 = float(input('enter b: '))
C1 = float(input('enter c: '))
A2 = float(input('enter a: '))
B2 = float(input('enter b: '))
C2 = float(input('enter c: '))
D=A1*B2 - A2*B1
if D > 0:
    x = (C1*B2 - C2*B1)/D
    y = (A1*C2 - A2*C1)/D
    print(f'x = {x}, y = {y}')
else:
    print('D<=0')