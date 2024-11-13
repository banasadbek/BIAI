Ax, Ay = map(float, input("Enter cordinates of A poin: ").split())
Bx, By = map(float, input("Enter cordinates of B poin: ").split())
side1 = Ay - By
side2 = Ax - Bx
if side1<0:
    side1 *=-1
if side2<0:
    side2 *=-1
P = 2*(side1+side2)
A = side1*side2
print("Perimeter =", P, "Area =", A)