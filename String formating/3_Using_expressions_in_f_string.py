# Using expressions in f-strings
# An f-string can include not only variables but also expressions inside curly braces {}.
# This makes the output dynamic and easy to read.

a = 10
b = 5

print(f"Sum of a and b is {a + b}")
print(f"Difference is {a - b}")
print(f"Product is {a * b}")
print(f"Division is {a / b}")

# Example with a condition
age = 20
print(f"You are {'adult' if age >= 18 else 'minor'}")
