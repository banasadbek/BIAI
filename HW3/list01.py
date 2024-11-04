def convert_cel_to_far(C):
    F = C*9/5 + 32
    return F
def convert_far_to_cel(F):
    C = (F-32) * 5/9
    return C

DF = float(input('Enter the degrees F: '))
print(f'{DF} degrees F = {round(convert_far_to_cel(DF), 2)} degrees C')

DC = float(input('Enter the degrees C: '))
print(f'{DC} degrees C = {round(convert_cel_to_far(DC), 2)} degrees F')