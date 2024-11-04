file = open('filename.txt', 'r')
text = file.read()
file.close()
words = text.replace(',', ' ').split()  # Replace commas with spaces
word_count = len(words)
print("Number of words in the file:", word_count)