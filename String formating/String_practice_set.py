# Interview Preparation: Strings and f-strings in Python
# This file contains common interview questions with answers and code examples.

# 1. What is a string in Python?
# Answer: A string is a sequence of characters enclosed in single, double, or triple quotes.
name = "Python"
print(name)

# 2. What is an f-string?
# Answer: An f-string lets you insert variables or expressions inside a string using braces {}.
age = 25
print(f"My age is {age}")

# 3. How do you concatenate strings?
# Answer: Use + or join().
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# 4. What is string slicing?
# Answer: Slicing extracts a part of a string using [start:end].
word = "Python"
print(word[0:3])   # Pyt
print(word[::-1])  # nohtyP

# 5. What are common string methods?
# Answer: upper(), lower(), strip(), replace(), split(), join(), find(), count()
text = "  Hello World  "
print(text.strip())
print(text.upper())
print(text.lower())
print(text.replace("World", "Python"))
print(text.split())

# 6. What is the difference between format() and f-string?
# Answer: f-string is shorter and easier to read.
score = 90
print("Score: {}".format(score))
print(f"Score: {score}")

# 7. Coding Question: Reverse a string
# Answer:
string = "python"
reversed_string = string[::-1]
print(reversed_string)

# 8. Coding Question: Check whether a string is a palindrome
# Answer:
text2 = "madam"
print(text2 == text2[::-1])

# 9. Coding Question: Count vowels in a string
# Answer:
word2 = "interview"
vowels = "aeiou"
count = sum(1 for ch in word2 if ch in vowels)
print(count)

# 10. Coding Question: Find the length of a string
# Answer:
message = "Hello"
print(len(message))

# 11. Coding Question: Remove spaces from a string
# Answer:
text3 = "Hello World"
print(text3.replace(" ", ""))

# 12. Coding Question: Capitalize the first letter of each word
# Answer:
text4 = "python interview questions"
print(text4.title())

# 13. Coding Question: Count the frequency of a character
# Answer:
sample = "banana"
print(sample.count("a"))

# 14. Coding Question: Print a string with expressions in f-string
# Answer:
num1 = 10
num2 = 20
print(f"Sum is {num1 + num2}")
print(f"Maximum is {max(num1, num2)}")

# 15. Coding Question: Format a number with 2 decimal places
# Answer:
price = 45.678
print(f"Price: {price:.2f}")

# 16. Interview Question: Why are f-strings preferred?
# Answer: They are faster, cleaner, and easier to read than old formatting methods.

# 17. Interview Question: What is the difference between immutable and mutable?
# Answer: Strings are immutable, meaning they cannot be changed once created.
name2 = "abc"
# name2[0] = "z"  # This would raise an error

# 18. Interview Question: How do you split a sentence into words?
# Answer:
sentence = "Python is easy"
print(sentence.split())

# 19. Coding Question: Join words into a sentence
# Answer:
words = ["Python", "is", "fun"]
print(" ".join(words))

# 20. Coding Question: Find the first repeated character
# Answer:
char_string = "programming"
seen = set()
first_repeat = None
for ch in char_string:
    if ch in seen:
        first_repeat = ch
        break
    seen.add(ch)
print(first_repeat)
