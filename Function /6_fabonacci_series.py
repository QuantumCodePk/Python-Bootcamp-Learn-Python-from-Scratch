# fabonacci_series.py
#
# Fibonacci series is a sequence where each number is the sum of the two preceding numbers.
# The sequence usually starts with 0 and 1.
#
# Syntax pattern for a function that generates Fibonacci numbers:
# def function_name(parameters):
#     # base cases
#     if condition:
#         return value
#     # recursive or iterative logic
#     return ...
#
# Example: generate the first n Fibonacci numbers using a function.

def fibonacci_sequence(n):
    """Return the first n Fibonacci numbers as a list."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence


def fibonacci_number(n):
    """Return the nth Fibonacci number (0-based index)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    print("First 8 Fibonacci numbers:", fibonacci_sequence(8))
    print("Fibonacci number at position 7:", fibonacci_number(7))


# Explanation:
# - Fibonacci series starts with 0 and 1.
# - Each next number is the sum of the previous two numbers.
# - fibonacci_sequence(n) returns the first n values in the series.
# - fibonacci_number(n) returns the nth Fibonacci number using iteration.
# - The function uses base cases for n <= 0 and n == 1.
# - Iteration continues until the desired position or list length is reached.
