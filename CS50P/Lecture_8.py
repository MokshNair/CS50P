"""
# Lecture 8: Object Oriented Programming

Object Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. It utilizes several techniques from previously established paradigms, including modularity, polymorphism, and encapsulation. The main idea behind OOP is to bind together the data and the functions that manipulate the data, so that no other part of the code can access this data except that function.


# tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets. for example;
ex_tuple = ("apple", "banana", "cherry")

# tuples vs lists
The main difference between tuples and lists is that tuples are immutable, meaning that you cannot change, add, or remove items after the tuple has been created. Lists, on the other hand, are mutable, which means that you can modify them after they have been created. For example;
ex_list = ["apple", "banana", "cherry"]
ex_list[0] = "kiwi"
print(ex_list)  # Output: ['kiwi', 'banana', 'cherry']

ex_tuple[0] = "kiwi"  # This will raise a TypeError because tuples are immutable



# Class

A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.

Classes have attributes and methods. Attributes are the data stored in an object, while methods are the functions that can be performed on the object. For example;
class Dog:
    def ex_class(self, name, age):
        self.name = name
        self.age = age


# Object

An object is an instance of a class. It is created from a class and has all the attributes and methods defined in the class. For example;
my_dog = Dog()
my_dog.ex_class("Buddy", 5)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5

# Instance variables are variables that are defined in a class and are specific to each instance of the class. They are created using the self keyword and can be accessed using the dot notation. 

# The __init__ method is used to initialize the instance variables of a class. It is called automatically when an object is created from the class. For example;
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# raise keyword is used to raise an exception. It is used to indicate that an error has occurred in the program. For example;
class Dog:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        

# __str__ method is used to define the string representation of an object. It is called when the object is printed or converted to a string. For example;
class Dog:
    def __str__(self):
        return f"{self.name} is {self.age} years old"

        
# properties
# A property is a special kind of attribute that is computed on the fly when it is accessed. It is defined using the @property decorator and can be accessed like a regular attribute. For example;
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return 3.14 * self.radius ** 2

        
# Getters and Setters
# Getters and setters are methods that are used to get and set the values of instance variables. They are defined using the @property decorator and can be accessed like regular attributes. For example;
class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")

# here, we have defined a getter for the radius property and a setter for the radius property. The getter returns the value of the _radius instance variable, while the setter checks if the value is negative and raises a ValueError if it is.



# @classmethod

It refers to a method that is bound to the class and not the instance of the class. It can be called on the class itself, rather than on an instance of the class. It is defined using the @classmethod decorator and takes the class as its first argument. 

# @staticmethod
It refers to a method that is bound to the class and not the instance of the class.



# inheritance

In Python we can inherit Parent classes to their children classes(sub-classes) by using "()" after the child class' name and before the ":", for example;

class Animalia:

# If "Animalia" is the Parent class, we can assign children classes as such;

class HomoSapien(Animalia):

# This signifies the class "HomoSapien" is a sub-class/child class of the super class/parent class "Animalia"

Imp. In order to use arguments from the Parent/Super class, we use the keyword "super()" 
(usually followed by the default __init__ method) for example; 

class Animalia:
    def __init__(self, species):
        if not species:
            raise ValueError("No Species entered!")
        self.species = species

class HomoSapien(Animalia):
    def __init__(self, species):
        super().__init__(species)

"""

"""
Problem Set 8

# Seasons of Love

# In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then  prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

Structure your program per the below, not only with a main function but also with one or more other functions as well:

from datetime import date

def main():
    ...

...

if __name__ == "__main__":
    main()

# Solution:
from datetime import date
import sys
import inflect

def main():
    
    dob_string = input("Date of Birth: ")
    try:
        birthDate = date.fromisoformat(dob_string)
        
    except ValueError:
        sys.exit("Invalid date")
        
    today = date.today()
    
    totalMinutes = calc_mins(birthDate, today)
    
    i = inflect.engine()
    words = str(i.number_to_words(totalMinutes, andword=""))
    
    print(f"{words.capitalize()} minutes")
    
    
def calc_mins(dob, today):
    
    timeDifference = today - dob
    
    totalTime = timeDifference.days * 24 * 60
    
    return totalTime


if __name__ == "__main__":
    main()
"""

"""
# Cookie Jar

Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:

__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
__str__ should return a str with 𝑛 🍪, where 𝑛 is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
capacity should return the cookie jar’s capacity.
size should return the number of cookies actually in the cookie jar, initially 0.
Structure your class per the below. You may not alter these methods’ parameters, but you may add your own methods.

class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

# Solution:

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity is a negative value!")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size
    
    def deposit(self, n):
        if n < 0:
            raise ValueError("Negative amount of cookies deposited!")
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies to deposit!")
        
        self._size += n
        

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Negative amount of cookies withdrawn!")
        if n > self._size:
            raise ValueError("More cookies withdrawn than in Jar!")
        
        self._size -= n
        
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
        
"""
"""
# CS50 Shirtificate


In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirt’s image should be centered horizontally.
The user’s name should be on top of the shirt, in white text.
All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim fpdf2’s API (application programming interface) to see all of its functions and parameters therefor.

# Solution:

from fpdf import FPDF 

name = input("Name: ")

pdf = FPDF(orientation="P", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 40)
pdf.cell(w=0, h=50, txt="CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=0, y=70, w=210)
pdf.set_text_color(255, 255, 255)
pdf.set_font("helvetica", "B", 24)
pdf.set_y(140)
pdf.cell(w=0, h=10, txt=name, align="C")

pdf.output("shirtificate.pdf")
"""