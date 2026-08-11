# Definition of a List in Python
# A list is a collection of items stored in one variable.
# It can hold multiple values, and the values can be changed later.
# Lists are written inside square brackets [] and can contain strings, numbers, or other data types.

#Creating a list:

numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, True]

#common operations on lists:
my_list = [1, 2, 3, 4, 5]
# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3
# Modifying elements
my_list[1] = 20
print(my_list)  # Output: [1, 20, 3, 4, 5]
# Adding elements
my_list.append(6)
print(my_list)  # Output: [1, 20, 3, 4, 5, 6]
# Removing elements
my_list.remove(3)
print(my_list)  # Output: [1, 20, 4, 5, 6]
# Length of the list
print(len(my_list))  # Output: 5    
# appending a list to another list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.append(list2)
print(list1)  # Output: [1, 2, 3, [4, 5, 6]]
# To merge two lists, use the extend() method
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]  



# Example
fruits = ["apple", "banana", "orange"]
print(fruits)
print(fruits[0])

# Adding an item to the list
fruits.append("grapes")
print(fruits)


# Create a list containing the table of 5
table_of_5 = [5 * i for i in range(1, 11)]
print(table_of_5)

a = 5
table = []
for i in range(1, 11):
    table.append(a * i)
print(table)