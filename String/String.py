# String
# Strings are sequences of characters enclosed in quotes.
# In Python, you can use single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Strings are immutable, which means their contents cannot be changed after creation.

# Examples:
name = 'Alice'
message = "Hello, world!"
multiline = '''This is a
multi-line string.'''

print(name)
print(message)
print(multiline)

# Common string operations:
print(len(message))
print(message.upper())
print(message.lower())
print(message.replace('world', 'Python'))
print('Hello' + ', ' + 'Python')
print(message[0])  # first character
print(message[7:12])  # substring