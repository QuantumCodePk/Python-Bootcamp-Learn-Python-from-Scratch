# Built-in String Functions
# Python provides built-in functions that work with strings.
# These functions can be used to get string length, convert case, and more.

text = "Hello, Python!"

# len() returns the number of characters in the string
length = len(text)
print(length)  # 14

# str() converts a value to a string
number = 42
print(str(number))  # '42'

# chr() returns the character for a Unicode code point
print(chr(65))  # 'A'

# ord() returns the Unicode code point for a character
print(ord('A'))  # 65

# max() and min() return the highest and lowest character by Unicode value
print(max(text))  # 'y'
print(min(text))  # ' '

# sorted() returns a list of sorted characters
print(sorted("banana"))  # ['a', 'a', 'a', 'b', 'n', 'n']

# any() checks whether any character in the string is truthy/non-empty
print(any(""))  # False
print(any("abc"))  # True

# all() checks whether all characters in the string are truthy/non-empty
print(all("abc"))  # True
print(all("a c"))  # True