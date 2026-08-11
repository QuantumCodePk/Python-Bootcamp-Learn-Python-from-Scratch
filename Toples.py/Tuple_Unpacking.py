# Tuple Unpacking in Python
# Tuple unpacking means assigning each item of a tuple to separate variables.

# Explanation
# - It makes code simpler and easier to read.
# - Each value in the tuple is assigned to a variable in order.
# - The number of variables must match the number of items in the tuple.

# Syntax
# variable1, variable2, variable3 = tuple_name

# Example
fruits = ("apple", "banana", "cherry")
fruit1, fruit2, fruit3 = fruits

print(fruit1)  # apple
print(fruit2)  # banana
print(fruit3)  # cherry

# Example with numbers
numbers = (10, 20, 30)
a, b, c = numbers
print(a)
print(b)
print(c)

# Using underscore for unused values
student = ("Rahul", 21, "Delhi")
name, age, _ = student
print(name)
print(age)
