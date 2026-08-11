'''
Function Scope and Lifetime in Python

Scope means where a variable can be used.
Lifetime means how long a variable stays in memory.

1. Local Scope
Variables created inside a function have local scope.
They can be used only inside that function.

Syntax:
def function_name():
    variable = value
    print(variable)

Example:
def greet():
    name = "Alice"
    print("Hello", name)

greet()

2. Global Scope
Variables created outside any function have global scope.
They can be used anywhere in the program.

Syntax:
variable = value

def function_name():
    print(variable)

Example:
message = "Welcome"

def show_message():
    print(message)

show_message()

3. Lifetime
- A local variable exists only while the function is running.
- A global variable exists until the program ends.

Example:
def test():
    x = 10
    print(x)

test()
# print(x)  # This will give an error because x is local to test()
'''
