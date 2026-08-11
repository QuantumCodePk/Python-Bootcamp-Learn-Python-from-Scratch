# Lambda_function.py
#
# Lambda functions are small anonymous functions in Python.
# They are defined with the keyword lambda and can take any number of arguments,
# but they can only contain a single expression.
#
# Syntax:
# lambda arguments: expression
#
# The expression is evaluated and returned automatically.
# Lambda functions are often used where a short, one-line function is needed.


# Example 1: a lambda function that adds two numbers.
add = lambda x, y: x + y
print("add(3, 4) =>", add(3, 4))


# Example 2: using a lambda with the built-in sorted() function.
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=lambda w: len(w))
print("sorted by length =>", sorted_words)


# Example 3: using lambda inside map() to square each number.
numbers = [1, 2, 3, 4]
squares = list(map(lambda n: n * n, numbers))
print("squares =>", squares)


# Explanation:
# - A lambda function is defined using lambda followed by its arguments,
#   a colon, and a single expression.
# - It is anonymous, meaning it does not need a name, although you can assign it to a variable.
# - Lambda functions are useful for short tasks like sorting, mapping, or filtering.
# - Use regular def functions when the logic is more than one expression or more readable.
