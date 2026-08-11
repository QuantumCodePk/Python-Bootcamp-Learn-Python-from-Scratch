# Definition of Set Operations in Python
# Set operations are operations performed on sets to combine, compare, or find common elements.

# Explanation
# - Sets can be used to perform mathematical operations like union, intersection, and difference.
# - These operations help us work with groups of unique values.

# Common set operations
# 1) Union: combines all unique elements from two sets
# 2) Intersection: finds common elements
# 3) Difference: finds elements in one set but not the other
# 4) Symmetric Difference: finds elements that are in one set or the other, but not both

# Example
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# Using method form
print("Union method:", set1.union(set2))
print("Intersection method:", set1.intersection(set2))
print("Difference method:", set1.difference(set2))
print("Symmetric Difference method:", set1.symmetric_difference(set2))

# Summary
# Set operations are used to compare and combine sets efficiently.
