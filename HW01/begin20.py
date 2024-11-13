Ax, Ay = map(float, input("Enter cordinates of A poin: ").split())
Bx, By = map(float, input("Enter cordinates of B poin: ").split())
length = ((By-Ay)**2+(Bx-Ax)**2)**(1/2)
print("Length =", length)