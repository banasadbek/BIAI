A = float(input("Enter A: "))
B = float(input("Enter B: "))
C = float(input("Enter C: "))
AB = B - A
BC = C - B
if AB <0:
    AB *= (-1)
if BC <0:
    BC *= (-1)
Total = AB+BC
print("AC =", AB, "BC =", BC, "Total =", Total)
