# Step Parameter
# The third value in a slice is the step, and it controls how many characters are skipped.
# Slice syntax: string[start:end:step]
# If step is omitted, the default is 1.

text = "abcdefghij"

# Step of 1 returns every character
print(text[0:10:1])  # 'abcdefghij'

# Step of 2 returns every second character
print(text[0:10:2])  # 'acegi'

# Step of 3 returns every third character
print(text[0:10:3])  # 'adgj'

# A negative step reverses the direction
print(text[9:0:-1])  # 'jihgfedcb'
print(text[::-1])     # 'jihgfedcba'

# You can combine omitted bounds with a step
print(text[::2])     # 'acegi'
print(text[1::2])    # 'bdfhj'

# Step is useful for patterns and reversing text without loops