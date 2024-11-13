file = open('filename.txt', 'r')
words = file.read().split()
max_length = len(max(words, key=len))
longest_words = [word for word in words if len(word) == max_length]
file.close()
print(longest_words)