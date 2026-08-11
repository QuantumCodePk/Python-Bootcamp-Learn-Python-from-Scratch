# String Methods and Functions
# Python strings have many built-in methods for analyzing and manipulating text.
# Common functions like len() also work with strings.

text = "  Welcome to Python methods and functions.  "

# len() returns the number of characters in the string
print(len(text))  # 40

# strip() removes whitespace from both ends
cleaned = text.strip()
print(cleaned)  # 'Welcome to Python methods and functions.'

# lower() and upper() change letter case
print(cleaned.lower())
print(cleaned.upper())

# replace() substitutes one substring for another
new_text = cleaned.replace("Python", "programming")
print(new_text)

# split() splits text into a list of words
words = cleaned.split()
print(words)

# join() combines a list of strings into one string
joined = " ".join(words)
print(joined)

# startswith() and endswith() check prefixes and suffixes
print(cleaned.startswith("Welcome"))
print(cleaned.endswith("functions."))

# find() returns the index of the first occurrence of a substring
pos = cleaned.find("methods")
print(pos)  # index where "methods" starts

# count() returns how many times a substring appears
print(cleaned.count("o"))

# title() and capitalize() format text
print(cleaned.title())
print(cleaned.capitalize())


