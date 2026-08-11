'''
Logical Operators
You might already be familiar with these! In logic, they are called logical connectives. These are also widely used in human language. They are: and, or and not.

and will only return True if both operands (the two boolean objects you are comparing) are True. For example:

print(True and True)
print(True and False)
print(False and False)


To understand the behavior of this logical operator, you can make use of a truth table:

a	      b	       a and b
True	True	True
True	False	False
False	True	False
False	False	False

'''

print(True and True and True and True)
print(True and True and True and False)
print(False or False or False or False)
print(False or False or False or True)