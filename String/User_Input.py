# The input function is used to take input from the user. It reads a line from input, converts it into a string (stripping a trailing newline), and returns that.

# by default, the input function returns the input as a string. If you want to convert the input to a different data type, you can use typecasting.

# Example of taking input from the user and converting it to an integer
user_input = input("Enter a number: ")  # Taking input from the user
print("You entered:", user_input)  # Printing the input


a = int(user_input)  # Converting the input to an integer
print("The input as an integer is:", a)  # Printing the converted input


# Comments, Escape Sequences, and String Formatting
# comments are used to explain the code and make it more readable. In Python, comments start with the hash character (#) and extend to the end of the physical line.
#
'''
Multi-line comments can be created using triple quotes 


'''

# 2 Escape Sequences
# Escape sequences are special characters that are used to represent certain whitespace or control characters in strings.
# For example, the escape sequence \n represents a newline character, and \t represents a
#    tab character. Escape sequences are used to format strings and control how they are displayed.

'''
1 \n - Newline
2 \t - Tab
3 \\ - Backslash
4 \' - Single Quote
5 \" - Double Quote
6 \r - Carriage Return
7 \b - Backspace
8 \f - Form Feed
9 \v - Vertical Tab
10 \ooo - Octal value
11 \xhh - Hex value
'''


# print statements with escape sequences
# Print () function is used to display output to the console. It can take multiple arguments and can be used to format strings using escape sequences.

print("Hello\nWorld")  # Output: Hello (newline) World
print("Hello\tWorld")  # Output: Hello (tab) World  

print("Hello\\World")  # Output: Hello\World
print("hello", "World", sep="-")  # Output: Hello-World
print("Hello", "World", end="!")  # Output: Hello World!
print("Hello", "World", sep="-", end="!")  # Output: Hello-World!
print("Hello", "World", sep="-", end="!\n")  # Output: Hello-World!






