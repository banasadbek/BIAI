n = 5 
file = open('filename.txt', 'r')
first_n_lines = [file.readline().strip() for _ in range(n)]
file.close()
print(first_n_lines)