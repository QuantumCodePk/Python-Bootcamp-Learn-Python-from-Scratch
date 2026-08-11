# indentation is important in Python, as it indicates a block of code. Make sure to use consistent indentation 
# (spaces or tabs) throughout your code.

# Comments are used to explain the code and are ignored by the Python interpreter. Use comments to describe what 
# your code does.

#variables are used to store data. In Python, you can create a variable by assigning a 
# value to it using the equals sign (=).

example_variable = "Hello, World!"  # This is a string variable
print(example_variable) 


#role of variables in programming is to store and manipulate data. They allow you to give a name to a value, 
# making it easier to reference and work with that value throughout your code.

#Python supports different data types, including integers, floats, strings, lists, tuples, dictionaries, and more.
integer_variable = 42  # This is an integer variable
float_variable = 3.14  # This is a float variable
string_variable = "Python is fun!"  # This is a string variable
Boolean_variable = True  # This is a boolean variable
is_valid = False  # This is another boolean variable
List_variable = [1, 2, 3, 4, 5]  # This is a list variable
# Lists are mutable, meaning you can change their contents after they are created. You can add, remove, or 
# modify elements in a list.

# mutable data types can be changed after they are created, while immutable data types cannot be changed after they 
# are created.

Tuple_variable = (1, 2, 3)  # This is a tuple variable
# Tuples are immutable, meaning you cannot change their contents after they are created. You cannot add, remove, or modify elements in a tuple.
Set_variable = {1, 2, 3}  # This is a set variable
# Sets are mutable, but they do not allow duplicate elements. You can add or remove elements from a set, but you cannot have two identical elements in a set.   

dictionary_variable = {"key1": "value1", "key2": "value2"}  
# example of a dictionary variable
a_dictionary = {"name": "Alice", "age": 30, "city": "New York"}
print(a_dictionary["name"])  # Output: Alice
print(a_dictionary["age"])   # Output: 30


# This is a dictionary variable
# Dictionaries are mutable, meaning you can change their contents after they are created. You can add, remove, or modify key-value pairs in a dictionary.   


#Example of different data types in Python, including integers, floats, strings, lists, tuples, dictionaries, and sets.



# Typecasting 
# type casting will convert one data type to other data type 
a =34
print(a)
print(type(a))


# Converting integer to float
b = float(a)
print(b)
print(type(b))


# converting float to integer
c = int(b)
print(c)
print(type(c))

# converting integer to string
d = str(c)
print(d)
print(type(d))

# converting string to integer
e = int(d)
print(e)
print(type(e))


