# Using format() Method
# The format() method inserts values into placeholders defined by {}.
# It is useful for building strings from variables.

name = "Alice"
age = 30

# Basic placeholder replacement
message = "Hello, {}. You are {} years old.".format(name, age)
print(message)

# Using numbered placeholders
message2 = "Hello, {0}. You are {1} years old. {0}, enjoy Python!".format(name, age)
print(message2)

# Using named placeholders
message3 = "Hello, {name}. You are {age} years old.".format(name=name, age=age)
print(message3)

# Formatting numbers with format()
price = 9.99
print("Price: ${:.2f}".format(price))  # two decimal places

# Align text with format()
print("{:<10} | {:^10} | {:>10}".format("left", "center", "right"))

# Using format() with dictionaries
person = {"name": "Bob", "age": 25}
print("Hello, {name}. You are {age} years old.".format(**person))