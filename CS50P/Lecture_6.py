"""
# File I/O
This lecture covers how to read and write files in Python. We will learn how to open a file, read its contents, and write to a file. We will also discuss the importance of closing files after we are done with them.


# list
Lists are a built-in data structure in Python that can hold an ordered collection of items. They are mutable, which means we can change their contents after they have been created. We can create a list using square brackets [] and separate the items with commas. For example:
my_list = [1, 2, 3, "Hello", "World"]
print(my_list)

In order to insert an item, like a user's input, into a list, we can use the append() method. For example:
my_list = []
user_input = input("Enter an item: ")
my_list.append(user_input)
print(my_list)


# open
To open a file in Python, we can use the built-in open() function. The open() function takes two arguments: the name of the file and the mode in which we want to open the file. The mode can be "r" for reading, "w" for writing, and "a" for appending. For example:
file = open("example.txt", "w")
file.write(name)
file.close()

This is different from # file = open("example.txt", "a") because the "w" mode will overwrite the existing contents of the file, while the "a" mode will append to the existing contents.



# with
The with statement in Python is used to wrap the execution of a block of code. It is often used when working with files to ensure that the file is properly closed after its suite finishes, even if an exception is raised. For example:

with open("example.txt", "w") as file:
    file.write(name)  


# readlines() is a method that reads all the lines of a file and returns them as a list. Each line in the file will be an element in the list. For example:

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)




    
# CSV - Comma Separated Values
CSV stands for Comma Separated Values. It is a file format that is used to store tabular data, such as a spreadsheet or a database. Each line in a CSV file represents a row of data, and each value in the row is separated by a comma. For example:
name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago

to open the CSV data, we can use the split() method to split the line into a list of values. For example:
with open("example.csv", "r") as file:
    for line in file:
        values = line.strip().split(",")
        print(values)


-----------------------------------------------------


file = open("students.csv", "w")
file.write("Hermione Granger, Gryffindor\n")
file.write("Harry Potter, Gryffindor\n")
file.write("Draco Malfoy, Slytherin\n")
file.write("Ron Weasley, Gryffindor\n")
file.close()

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)


def get_name(student):
    return student["name"]

# In order to sort the students by their names, we can use the sorted() function and pass in the get_name function as the key. This will sort the students based on their names. For example:
for student in sorted(students, key= get_name):
    print(f"{student['name']} is in {student['house']}")

# Here, the sorted() function will use the get_name function to sort every dictionary in the file by the value of the "name" key.


# Lambda Functions

# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. It is often used as a key function in sorting. For example:

students = [
    {"name": "Hermione Granger", "house": "Gryffindor"},
    {"name": "Harry Potter", "house": "Gryffindor"},    
    {"name": "Draco Malfoy", "house": "Slytherin"},
    {"name": "Ron Weasley", "house": "Gryffindor"}
]

for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")



    
# CSV Package

# The csv module in Python provides functionality to read and write CSV files. It allows us to easily handle CSV data without having to manually split lines and manage the formatting. For example:

file = open("students.csv", "w")
file.write("Harry, Number 4, Privet Drive\n")
file.write("Hermione, Number 12 Grimmauld Place\n")
file.write("Ron, The Burrow\n")

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        students.append({"name": line[0], "home": line[1]})
                        
for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# In order to read a CSV file with multiple commas, we can use the csv.DictReader() function, which will read the CSV file and return each row as a dictionary. For example:
file = open("students.csv", "w")
file.write("name,home\n")
file.write("Harry,\"Number 4, Privet Drive\"\n")
file.write("Hermione, Number 12 Grimmauld Place\n")
file.write("Ron, The Burrow\n") 
file.close()

import csv

from streamlit import user
students = []
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for line in reader:
        students.append({"name": line["name"], "home": line["home"]})

for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# the difference between csv.reader() and csv.DictReader() is that csv.reader() returns each row as a list, while csv.DictReader() returns each row as a dictionary, where the keys are the column headers and the values are the corresponding values in the row.


# How to take input from the user into a CSV file?

To take input from the user into a CSV file, we can use the csv.writer() function to write the user's input to the CSV file. For example:

import csv

with open("students.csv", "w") as file:
    writer = csv.writer(file)
    name = input("Name: ")
    home = input("Home: ")
    writer.writerow([name, home])

# We can also use the csv.DictWriter() function to write the user's input to the CSV file as a dictionary. For example:

import csv
with open("students.csv", "w") as file:
    fieldnames = ["name", "home"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    name = input("Name: ")
    home = input("Home: ")
    writer.writerow({"name": name, "home": home})

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(f"{line['name']} is from {line['home']}")

# The difference again is that csv.writer() writes the user's input as a list, while csv.DictWriter() writes the user's input as a dictionary, where the keys are the column headers and the values are the corresponding values in the row.

# The benefit of using the DictReader() and DictWriter() functions is that they allow us to easily access the values in the CSV file using the column headers as keys, which can make our code more readable and easier to maintain.

"""

"""
Problem Set 6 - File I/O

# Lines of Code

In a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.



import sys

# We will first check if there is only one Command Line Argument passed and whether or not it is the name of a Python file.

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")


# We will then check whether or not the file name put in through the CLA, exists. If it does, we will proceed ahead and count all the valid lines and then print the count.

fileName = sys.argv[1]
count = 0

try:
    with open(fileName) as file:
        for line in file:
            if line.strip() == "":
                continue
            elif line.lstrip().startswith("#"):
                continue
            else:
                count = count + 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(count)



# Pizza Py

In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.


    
import tabulate
import csv
import sys

if len(sys.argv) < 2:
    sys.exit("No CSV file entered")

elif len(sys.argv) > 2:
    sys.exit("Multiple input entered")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

userInput = sys.argv[1]

try:
    with open(userInput,"r") as file:
        reader = csv.reader(file)
        data = list(reader)

        if not data:
            print("The CSV file is empty.")
        
        print(tabulate.tabulate(data, headers= "firstrow" ,tablefmt = "grid"))

except FileNotFoundError:
    sys.exit("File does not exist")

"""

"""
# Scourgify

In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.


import sys
import csv

# We will first check for valid CLA passed.

if len(sys.argv) != 3:
    sys.exit("Too few/many Command-Line Arguments")

oldFile = sys.argv[1]
newFile = sys.argv[2]

students = []

try:
    with open(oldFile) as file:
        reader = csv.DictReader(file)
        for line in reader:
            student = {}
            fullName = line["name"]
            lName, fName = fullName.split(", ") 
            house = line["house"]
            student["first"] = fName.strip()
            student["last"] = lName.strip()
            student["house"] = house.strip()
            students.append(student)

    with open(newFile, "w", newline= "") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


except FileNotFoundError:
    sys.exit("File not found")

"""