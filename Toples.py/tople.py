# Python Tuple
# A tuple is an ordered, immutable collection of items.
# It is similar to a list, but once created, its values cannot be changed.

# Explanation
# - Tuples are used to store multiple values in one variable.
# - They are ordered, so items have a defined position.
# - They are immutable, so you cannot add, remove, or change items after creation.
# - Tuples can hold duplicate values.
# - They can contain different data types.

# Syntax
# Empty tuple
empty_tuple = ()

# Tuple with values
numbers = (10, 20, 30, 40)

# Single-item tuple (comma is required)
single_item = (50,)

# Example
fruits = ("apple", "banana", "cherry")
print(fruits)           # ('apple', 'banana', 'cherry')
print(fruits[0])        # apple
print(fruits[-1])       # cherry

# Accessing multiple items using slicing
print(fruits[0:2])      # ('apple', 'banana')

# Iterating through a tuple
for fruit in fruits:
    print(fruit)

# Tuple unpacking
name1, name2, name3 = fruits
print(name1)            # apple
print(name2)            # banana
print(name3)            # cherry

# Built-in tuple methods
# Tuple has only two built-in methods:

# 1) count(value)
# Returns the number of times a value appears in the tuple.
print(fruits.count("apple"))   # 1

# 2) index(value)
# Returns the index of the first occurrence of a value.
print(fruits.index("banana"))  # 1

# Difference between tuple and list
# - List uses [] and is mutable.
# - Tuple uses () and is immutable.

# Example of immutability
# This line would raise an error:
# fruits[0] = "mango"
