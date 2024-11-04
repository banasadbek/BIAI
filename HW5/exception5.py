try:
    f = open('Filename', 'w')
    print(f)
except PermissionError:
    print('Permission Error')