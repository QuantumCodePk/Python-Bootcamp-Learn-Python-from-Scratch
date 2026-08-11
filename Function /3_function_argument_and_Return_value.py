# function_argument_and_Return_value.py
#
# This example shows how to pass arguments into a function
# and how a function returns a result back to the caller.
#
# Arguments are values you provide when calling the function.
# The return value is what the function sends back after it finishes.


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def build_message(name, score):
    """Build a formatted message using the provided arguments."""
    return f"{name} scored {score} points."


def greet_user(name, greeting="Hello"):
    """Show how default arguments work when a value is omitted."""
    return f"{greeting}, {name}!"


def describe_product(name, price, currency="USD"):
    """Show a product description using a default currency argument."""
    return f"{name} costs {price} {currency}."


if __name__ == "__main__":
    x = 4
    y = 7
    product = multiply(x, y)
    print(f"multiply({x}, {y}) returns: {product}")

    student = "Aisha"
    total_score = 95
    message = build_message(student, total_score)
    print(message)

    # Positional argument example: order matters for non-keyword arguments.
    print(greet_user("Aisha", "Hi"))

    # Keyword argument example: parameter names are specified explicitly.
    print(greet_user(name="Aisha", greeting="Hi"))
    print(greet_user(greeting="Hi", name="Aisha"))
    
    # Default argument example: greeting uses the default value when omitted.
    print(greet_user("Aisha"))

    # Using the default currency argument.
    print(describe_product("Book", 12.99))
    # Overriding the default argument with a specific value.
    print(describe_product("Book", 12.99, "EUR"))
    # Keyword argument usage with a default argument.
    print(describe_product(name="Notebook", price=8.5, currency="CAD"))


# Explanation:
# - multiply(a, b) receives two positional arguments and returns their product.
# - build_message(name, score) receives two positional arguments and returns text.
# - greet_user(name, greeting="Hello") has a default argument, so greeting is optional.
# - describe_product(name, price, currency="USD") uses currency="USD" when no currency is provided.
# - Positional arguments are passed in order: the first value maps to the first parameter.
# - Keyword arguments let you specify parameter names explicitly and can appear in any order.
# - Default arguments supply a value automatically when the caller omits that argument.
# - The caller can still override default arguments by passing a value explicitly.
