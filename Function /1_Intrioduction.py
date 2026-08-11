# Python functions and modules
#
# A function is a reusable block of code that performs a specific task.
# You define a function with def, call it by name, and can pass arguments.
# A module is a Python file that contains functions, classes, and variables.
# You can import a module into another file and use its contents.

# Example: define a function in this file

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}! Welcome to Python."


# Example: define another function that uses a small calculation

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


# When this file is run directly, the code below executes.
if __name__ == "__main__":
    print(greet("Student"))
    print("2 + 3 =", add_numbers(2, 3))


# If this file were used as a module, another file could import it like this:
# from Intrioduction import greet, add_numbers
# print(greet("Alice"))
# print(add_numbers(5, 7))
