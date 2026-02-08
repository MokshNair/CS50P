"""
Docstring for CS50P.Lecture_1

#
# Comparing two integers using "Conditionals"

x = int(input("What is X? "))
y = int(input("What is Y? "))

if x < y:
    print("X is lesser than Y!")
elif x > y:
    print("X is greater than Y!")
else:
    print("X is equal to Y!")
    
# OR

if x < y or x > y:
    print("X is not equal to Y!")
else:
    print("X is equal to Y!")

# OR

if x != y:
    print("X is not equal to Y!")
else:
    print("X is equal to Y!")


#
# Grading a student based on their score:

score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

    


#
# Is a number even or odd? (But using Functions & Conditionals!)

def main():
    x = int(input("What is X? "))
    if is_even(x):
        print("Even!")
    else:
        print("Odd!")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()

# OR
# def is_even(n):
#   return True if n % 2 == 0 else False
# OR
#   return n % 2 == 0
# #


#
# Using "match" and "case":

name = input("What is your name? ").strip().title()

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor!")
    case "Draco":
        print("Slytherin!")
    case _:
        print("Who?")

"""
"""
# Problem Set 1:
# 
# Deep Thought | deep.py
# 
# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
#
#
# answer = str(input("What is the answer to the Great Question of Life, the Universe and Everything? ")).lower().strip()
# match answer:
#    case "42" | "forty-two" | "forty two":
#        print("Yes")
#    case _:
#        print("No")



# Home Federal Savings Bank | bank.py
# 
# In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.
#In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
# 
# 
# greeting = input("Greeting: ").strip().lower()
# hello = "hello"
#
# if hello in greeting:
#    print("$0")
# elif greeting[0] == "h":
#    print("$20")
# else:
#    print("$100")


# File Extensions | extensions.py
# 
# Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name. For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

# Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg. To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.
#See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
#.gif .jpg .jpeg .png .pdf .txt .zip

# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

extension = str(input("File name: ")).strip().lower()

match extension:
    case a if ".gif" in extension:
        print("image/gif")
    case a if ".jpg" in extension:
        print("image/jpeg")
    case a if ".jpeg" in extension:
        print("image/jpeg")
    case a if ".png" in extension:
        print("image/png")
    case a if ".pdf" in extension:
        print("application/pdf")
    case a if ".txt" in extension:
        print("text/plain")
    case a if ".zip" in extension:
        print("application/zip")
    case _:
        print("application/octet-stream")


# Math Interpreter | interpreter.py
# 
# Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

#In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

#Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

expression = input("Expression: ").strip()
x, y, z = expression.split(" ")
x = int(x)
z = int(z)

match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        print(float(x / z))
    case _:
        print("Invalid values")



# Meal Time | meal.py
# 
# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

# In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).#

# 7 to 8 = breakfast
# 12 to 1 = lunch
# 6 to 7 = dinner

def main():
    time = input("What time is it? ").strip().lower()
    float_time = convert(time)

    if 7.0 <= float_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= float_time <= 13.0:
        print("lunch time")
    elif 18.0 <= float_time <= 19.0:
        print("dinner time")

def convert(time):
    if " " in time:
        time_part, suffix = time.split(" ")
        hour, minute = time_part.split(":")
        hour = int(hour)
        minute = int(minute)

        if "p.m" in suffix and hour != 12:
            hour += 12
        elif "a.m" in suffix and hour == 12:
            hour = 0
    
    else:
        hour, minute = time.split(":")
    
    return (int(hour) + int(minute)/60)
        

if __name__ == "__main__":
    main()

"""