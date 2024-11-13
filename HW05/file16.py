file = open('filename.txt', 'r')
is_closed = file.closed
print("File is closed:", is_closed)
file.close()
is_closed_after_close = file.closed
print("File is closed after closing:", is_closed_after_close)