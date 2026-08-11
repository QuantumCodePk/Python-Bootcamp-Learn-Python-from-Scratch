# Removing Whitespace
# Python strings provide methods to remove whitespace from the beginning, end, or both.

text = "   Hello, Python!   "

# strip() removes whitespace from both ends
cleaned = text.strip()
print(repr(cleaned))  # 'Hello, Python!'

# lstrip() removes whitespace from the left only
left_cleaned = text.lstrip()
print(repr(left_cleaned))  # 'Hello, Python!   '

# rstrip() removes whitespace from the right only
right_cleaned = text.rstrip()
print(repr(right_cleaned))  # '   Hello, Python!'

# strip() can also remove specified characters
text2 = "---Hello---"
print(text2.strip('-'))  # 'Hello'

# Original string remains unchanged
print(repr(text))  # '   Hello, Python!   '