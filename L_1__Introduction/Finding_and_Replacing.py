# Finding and Replacing
# Python strings let you search for substrings and replace them with other text.

text = "Python is fun. Learning Python is rewarding."

# find() returns the index of the first occurrence, or -1 if not found
index = text.find("Python")
print(index)  # 0

# rfind() returns the index of the last occurrence
last_index = text.rfind("Python")
print(last_index)  # 20

# count() returns how many times a substring appears
count = text.count("Python")
print(count)  # 2

# replace() substitutes all occurrences by default
updated = text.replace("Python", "coding")
print(updated)  # 'coding is fun. Learning coding is rewarding.'

# replace() can also change only the first n occurrences
partial_update = text.replace("Python", "coding", 1)
print(partial_update)  # 'coding is fun. Learning Python is rewarding.'

# The original string is unchanged
print(text)