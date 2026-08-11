# Formatting numbers in f-strings
# We can control how numbers appear by using format specifiers inside curly braces.
# For example, :.2f shows a number with 2 decimal places.

price = 19.456
print(f"Price: {price:.2f}")

# :,.2f adds commas and two decimal places
amount = 1234567.89
print(f"Amount: {amount:,.2f}")

# :08d shows the number with leading zeros up to 8 digits
number = 42
print(f"Number: {number:08d}")
