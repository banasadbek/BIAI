try:
    f = open('filename', 'r')
    print('File found!')
except FileNotFoundError:
    print('File not found')