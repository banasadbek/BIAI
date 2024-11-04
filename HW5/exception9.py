with open('text.txt', 'w', encoding='utf-16') as f:
    f.write('This is some text')

try:
    f = open('text.txt', 'r')
    print(f.read())
except UnicodeDecodeError:
    print('Encoding issue has occurred')
