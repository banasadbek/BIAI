r1 = -1
r2 = -1
while r2<0 or r1<0:
    print('Enter a value not zero')
    r1 = float(input("Enter radius 1: "))
    r2 = float(input("Enter radius 2: "))
pi = 3.14
S1 = pi*(r1**2)
S2 = pi*(r2**2)
S3 = pi*(r2**2-r1**2)
print('S1, S2, S3 are', S1,S2,S3, 'respectively')