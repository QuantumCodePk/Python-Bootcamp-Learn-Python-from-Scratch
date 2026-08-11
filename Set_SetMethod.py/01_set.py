# Set in Python
# A set is an unordered collection of unique items.
# It is used to store distinct values and perform mathematical set operations.

# Explanation
# - Sets are unordered, so items do not have a fixed index.
# - Sets cannot contain duplicate values.
# - Sets are mutable, so you can add or remove items.
# - Sets are useful for membership testing and removing duplicates.

# Syntax
# Creating an empty set
empty_set = set()

# Creating a set with values
numbers = {1, 2, 3, 4}

# Example
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Adding items
fruits.add("mango")
print(fruits)

# Removing an item
fruits.remove("banana")
print(fruits)

# Common set methods
# 1) add(value)
fruits.add("grape")
print(fruits)

# 2) remove(value)
fruits.remove("apple")
print(fruits)

# 3) discard(value)
fruits.discard("orange")  # does not raise error if value is not present
print(fruits)

# 4) pop()
print(fruits.pop())

# 5) clear()
fruits.clear()
print(fruits)

# 6) union(other_set)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# 7) intersection(other_set)
print(set1.intersection(set2))

# 8) difference(other_set)
print(set1.difference(set2))

# 9) symmetric_difference(other_set)
print(set1.symmetric_difference(set2))

# 10) update(other_set)
set3 = {1, 2}
set4 = {3, 4}
set3.update(set4)
print(set3)

# 11) copy()
copy_set = set3.copy()
print(copy_set)

# 12) len()
print(len(set3))
