"""

# If we were to ask the user for a positive number, to perform iterations, we can use a while loop to keep prompting the user until they provide a valid input, we can use the following code:

while True:
# This will create an infinite loop, which will keep running until we break out of it. Inside the loop, we ask the user for input and check if it's a positive number. If it is, we break out of the loop; otherwise, we print an error message and prompt again.
    n = int(input("Enter a positive number: "))
    if n > 0:
        break
    print("Invalid input. Please enter a positive number.")
print("Meow!" * n)


# LISTS:

# A list is a collection of items that are ordered and changeable. Lists are defined using square brackets [] and can contain any type of data, including other lists. For example:
fruits = ["apple", "banana", "cherry"]

# To access an item in a list, we can use its index, which starts at 0. For example:
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

# We can also use a for loop to iterate over the items in a list. For example:
for fruit in fruits:
    print(fruit)  



# DICTIONARIES:

# A dictionary is a collection of key-value pairs that are unordered and changeable. Dictionaries are defined using curly braces {} and each key is separated from its value by a colon :. For example:
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}     
# To access a value in a dictionary, we can use its key. For example:
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30
print(person["city"])  # Output: New York

# We can also use a for loop to iterate over the key-value pairs in a dictionary. For example:
for key, value in person.items():
    print(f"{key}: {value}")    



# DICTIONARIES WITHIN LISTS:
# We can also have dictionaries within lists, which allows us to store more complex data structures. For example:

students = [
    {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
    {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"Name": "Draco", "House": "Slytherin", "Patronus": None}
]

for student in students:
    print(student["Name"], student["House"], student["Patronus"], sep=", ")


"""