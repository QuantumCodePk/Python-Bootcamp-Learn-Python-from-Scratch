# String Indexing
# Strings in Python are ordered sequences of characters.
# Each character has an index, starting at 0 for the first character.
# You can use square brackets [] to access specific characters by index.

text = "Python"

# Positive indexing:
print(text[0])  # 'P'
print(text[1])  # 'y'
print(text[5])  # 'n'

# Negative indexing starts from the end:
print(text[-1])  # 'n'
print(text[-2])  # 'o'

# Indexing is useful for getting individual characters:
first_char = text[0]
last_char = text[-1]
print(f"First character: {first_char}")
print(f"Last character: {last_char}")

# Trying to access an index outside the string length raises an error:
# print(text[6])  # IndexError: string index out of range