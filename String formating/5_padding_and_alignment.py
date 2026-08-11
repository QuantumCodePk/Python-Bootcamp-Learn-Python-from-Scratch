# Padding and alignment in f-strings
# We can add spaces around values to align text neatly in columns.
# :<10 means left align in a field of width 10.
# :>10 means right align in a field of width 10.
# :^10 means center align in a field of width 10.

name = "Aman"
print(f"{name:<10}END")
print(f"{name:>10}END")
print(f"{name:^10}END")

# Example with numbers
number = 42
print(f"{number:<10}done")
print(f"{number:>10}done")
print(f"{number:^10}done")
