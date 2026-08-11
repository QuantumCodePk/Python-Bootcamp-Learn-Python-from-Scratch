# Definition of Set Methods in Python
# Set methods are built-in functions that work on sets.
# They are used to perform operations such as adding, removing, combining, or comparing sets.

# Explanation
# - A set is a collection of unique items.
# - Set methods help us manipulate the set easily.
# - They are called using dot notation, for example: set_name.method().

# Common set methods
# 1) add(value) -> adds an element to the set
# 2) remove(value) -> removes an element; raises an error if it does not exist
# 3) discard(value) -> removes an element without raising an error
# 4) pop() -> removes and returns a random element
# 5) clear() -> removes all elements from the set
# 6) union(set2) -> returns a new set with all unique elements from both sets
# 7) intersection(set2) -> returns common elements
# 8) difference(set2) -> returns elements present in the first set but not in the second
# 9) symmetric_difference(set2) -> returns elements that are in one set but not both
# 10) update(set2) -> adds elements from another set

# Example
fruits = {"apple", "banana", "cherry"}
fruits.add("mango")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("orange")
print(fruits)

print(fruits.pop())
print(fruits)

fruits.clear()
print(fruits)

# Summary
# Set methods are used to modify and work with sets efficiently.
