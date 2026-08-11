# String Slicing
# Slicing lets you extract a substring from a string using start:end:step.
# The slice includes the start index and excludes the end index.

text = "Hello, Python!"

# Basic slicing: characters from index 0 to 4 (exclusive end)
print(text[0:5])  # 'Hello'

# Omitting start uses the beginning of the string
print(text[:5])  # 'Hello'

# Omitting end uses the end of the string
print(text[7:])  # 'Python!'

# Negative indexes count from the end
print(text[-7:-1])  # 'Python'

# Step allows skipping characters
print(text[0:11:2])  # 'Hlo y'

# Reverse a string with slicing step -1
print(text[::-1])  # '!nohtyP ,olleH'

# Slicing is a safe way to get substrings without modifying the original string
substring = text[7:13]
print(substring)  # 'Python'