a = list(map(int, input('Enter the initial list: ').split()))
start, end = map(int, input('Enter the starting and ending: ').split())
print(min(a[start:end]))