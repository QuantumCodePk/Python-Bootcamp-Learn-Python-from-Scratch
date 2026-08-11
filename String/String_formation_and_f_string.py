# String Formatting and f-strings
# Python provides several ways to build strings with dynamic values.
# f-strings are the most modern and readable method (Python 3.6+).

name = "Alice"
age = 25

# Using concatenation
greeting1 = "Hello, " + name + "!"
print(greeting1)

# Using format()
greeting2 = "Hello, {}! You are {} years old.".format(name, age)
print(greeting2)

# Using f-strings (recommended)
greeting3 = f"Hello, {name}! You are {age} years old."
print(greeting3)

# f-strings can include expressions directly
result = f"Next year, you will be {age + 1}."
print(result)

# Formatting numbers inside f-strings
price = 19.99
print(f"Price: ${price:.2f}")  # two decimal places

# Multi-line strings with variables
message = f"""Dear {name},
Your appointment is scheduled for tomorrow.
Thank you!"""
print(message)


