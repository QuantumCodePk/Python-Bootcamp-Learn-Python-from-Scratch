# Splitting and Joining
# split() breaks a string into a list using a separator.
# join() combines a list of strings into one string with a separator.

text = "apple,banana,cherry"

# split() using comma as delimiter
fruits = text.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']

# split() without argument splits on whitespace
sentence = "Python is easy to learn"
words = sentence.split()
print(words)  # ['Python', 'is', 'easy', 'to', 'learn']

# join() uses a string as separator to combine list items
joined = "-".join(fruits)
print(joined)  # 'apple-banana-cherry'

# join() can also reassemble a sentence
reassembled = " ".join(words)
print(reassembled)  # 'Python is easy to learn'

# split() with maxsplit limits the number of splits
limited = sentence.split(" ", 2)
print(limited)  # ['Python', 'is', 'easy to learn']

# Using splitlines() to split text at line breaks
multiline = "Line1\nLine2\nLine3"
lines = multiline.splitlines()
print(lines)  # ['Line1', 'Line2', 'Line3']