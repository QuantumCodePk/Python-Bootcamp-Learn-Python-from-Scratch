# Changing Case
# Python strings include methods to convert text to upper case, lower case, title case, and more.

text = "Python String CASE Example"

# Convert to lowercase
lower_text = text.lower()
print(lower_text)  # 'python string case example'

# Convert to uppercase
upper_text = text.upper()
print(upper_text)  # 'PYTHON STRING CASE EXAMPLE'

# Convert to title case
title_text = text.title()
print(title_text)  # 'Python String Case Example'

# Capitalize the first letter of the string
capitalized_text = text.capitalize()
print(capitalized_text)  # 'Python string case example'

# Swap case for each character
swapped_text = text.swapcase()
print(swapped_text)  # 'pYTHON sTRING case eXAMPLE'

# Case methods return a new string and do not change the original
print(text)  # original string remains unchanged