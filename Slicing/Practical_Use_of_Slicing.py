# Practical Use of Slicing
# Slicing is useful for extracting substrings, removing parts, and processing text.
# It works with strings, lists, and other sequence types.

text = "Python programming is fun"

# Extract a word by slicing the relevant index range
word = text[0:6]
print(word)  # 'Python'

# Remove the first and last characters
trimmed = text[1:-1]
print(trimmed)  # 'ython programming is fu'

# Take every second character for pattern use
pattern = text[::2]
print(pattern)  # 'Pto rgamn s f'

# Reverse the string with slicing
reversed_text = text[::-1]
print(reversed_text)  # 'nuf si gnimmargorp nohtyP'

# Slice a list to work with part of a sequence
items = [10, 20, 30, 40, 50]
print(items[1:4])  # [20, 30, 40]

# Use negative indexes for end-based slicing
print(items[-3:])  # [30, 40, 50]

# Use slicing to skip the first two characters and keep every third one
print(text[2::3])  # 'to rgm s '

# Practical use: get the first sentence from a paragraph
paragraph = "Hello world. Welcome to Python. Learn slicing."
end = paragraph.find('.') + 1
first_sentence = paragraph[:end]
print(first_sentence)  # 'Hello world.'