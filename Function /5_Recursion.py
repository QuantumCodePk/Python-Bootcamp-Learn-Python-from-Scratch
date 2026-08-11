# Recursion.py
#
# Recursion is when a function calls itself to solve a smaller part of the problem.
# A recursive function needs at least one base case to stop calling itself.
#
# Syntax pattern:
# def function_name(parameters):
#     if base_condition:
#         return base_value
#     else:
#         return function_name(smaller_input)
#
# The base case prevents infinite recursion and lets the function return a result.


def factorial(n):
    """Return n! (n factorial) using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Return the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("factorial(5) =>", factorial(5))
    print("fibonacci(7) =>", fibonacci(7))


# Explanation:
# - recursion means a function calls itself.
# - The base case stops the recursion and returns a simple result.
# - In factorial(), the base case is n <= 1.
# - In fibonacci(), the base cases are n <= 0 and n == 1.
# - Each recursive step works on a smaller input until the base case is reached.
