# Checking String Properties
# Python strings provide methods to check the contents of the string.
# These methods return True or False based on the string's characters.

text = "Python123"

# isalpha() checks if all characters are letters
print(text.isalpha())  # False
print("Python".isalpha())  # True

# isdigit() checks if all characters are digits
print(text.isdigit())  # False
print("12345".isdigit())  # True

# isalnum() checks if all characters are letters or digits
print(text.isalnum())  # True
print("Python 3".isalnum())  # False because of the space

# islower() and isupper() check letter case
print("python".islower())  # True
print("PYTHON".isupper())  # True

# isspace() checks if the string contains only whitespace
print("   ".isspace())  # True
print(" \t\n".isspace())  # True

# startswith() and endswith() check prefixes and suffixes
print(text.startswith("Py"))  # True
print(text.endswith("123"))  # True

# These checks are useful for validating input before processing it.