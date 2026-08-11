# String Methods
# Python strings have built-in methods that make common text operations easy.
# These methods do not modify the original string; they return a new string.

text = "  Hello, Python learners!  "

# strip() removes whitespace from both ends
cleaned = text.strip()
print(cleaned)  # 'Hello, Python learners!'

# lower() converts to lowercase
print(cleaned.lower())  # 'hello, python learners!'

# upper() converts to uppercase
print(cleaned.upper())  # 'HELLO, PYTHON LEARNERS!'

# replace() replaces a substring with another substring
updated = cleaned.replace("Python", "world")
print(updated)  # 'Hello, world learners!'

# split() divides a string into a list of parts
words = cleaned.split()
print(words)  # ['Hello,', 'Python', 'learners!']

# find() returns the index of the first match, or -1 if not found
pos = cleaned.find("Python")
print(pos)  # 7

# count() returns how many times a substring appears
count = cleaned.count("o")
print(count)  # 2

# isalpha() checks whether the string contains only letters
print("Hello".isalpha())  # True
print("Hello123".isalpha())  # False