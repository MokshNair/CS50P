"""
Docstring for CS50P.Lecture_0

Let's say Hello to the user!

# Ask the user for their name
name = input("What is your name? ")

# Strip any leading or trailing whitespace from the input, and also capitalize the first and last name
name = name.strip().title()

# What if we want to greet the user with their first name only?
# We can split the name into parts using the split() method, which splits the string at spaces by default
first_name, surname = name.split(" ")

# Greet the user with their first name *using a Format String, i.e., f("abc {xyz}")*
print(f"Hello, {first_name}!")

"""

# Calculator.py:

# x = input("What is X? : ")
# y = input("What is Y? : ")
# z = int(x) + int(y)
#   and if the user enters a non-integer value, the program will crash. To prevent this, we can use the float() function instead of int(), which can handle decimal numbers as well.
#   dditionally, we can round the sum up using the round() function, i.e., z = round(x + y)
# print("Sum of X and Y is :", z)
# OR
# x = int(input("What is X? : "))
# y = int(input("What is Y? : "))
# print("Sum of X and Y is :", x + y)


# to add differentiators to a number (for ex. 1,000), we can use formatted strings as follows:
# z = 100000
# print(f"{z:,}")

"""

How to define a function in Python?

# def greet(name):
#     print(f"Hello, {name}!")  

and to call the function, we simply use its name followed by parentheses, passing any required arguments inside the parentheses, i.e.,

# greet("Moksh")
output: Hello, Moksh!

for example;

def greet(name):
    print(f"Hello, {name}!")

greet(input("What is your name? ").title().strip())

What if we want to return a value from a function instead of printing it directly?

def greet(name):
    return f"Hello, {name}!"

greeting = greet(input("What is your name? ").title().strip())
print(greeting)

output: Hello, Moksh!

"""
