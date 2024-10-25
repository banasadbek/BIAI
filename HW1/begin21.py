x1, y1 = map(float, input("Enter cordinates of A poin: ").split())
x2, y2 = map(float, input("Enter cordinates of B poin: ").split())
x3, y3 = map(float, input("Enter cordinates of C poin: ").split())
side1 = (((x1-x2)**2)+((y1-y2)**2))**(1/2)
side2 = (((x1-x3)**2)+((y1-y3)**2))**(1/2)
side3 = (((x2-x3)**2)+((y2-y3)**2))**(1/2)
P =(side1 + side2 + side3)/2
Area = (P*(P-side1)*(P-side2)*(P-side3))**(1/2)
print("Perimeter =", P*2, "Area =", Area)