'''
Break, Continue, and Pass in Python

These are control statements used inside loops.

1. break
The break statement stops the loop immediately.

Syntax:
for item in sequence:
    if condition:
        break

Example:
for i in range(1, 6):
    if i == 3:
        break
    print(i)

2. continue
The continue statement skips the current iteration and moves to the next one.

Syntax:
for item in sequence:
    if condition:
        continue
    print(item)

Example:
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

3. pass
The pass statement is a placeholder. It does nothing and is used when you want a block to exist without writing code yet.

Syntax:
def function_name():
    pass

Example:
for i in range(1, 4):
    if i == 2:
        pass
    else:
        print(i)
'''
