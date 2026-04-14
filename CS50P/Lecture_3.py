"""
Lecture 3: Exceptions

Exceptions are errors that occur during the execution of a program. They can be handled using try and except blocks.


try:
# try block is used to wrap code that may raise an exception. If an exception occurs, the code in the except block will be executed.
    x = int(input("Enter a number: "))

except ValueError:
# except block is used to handle specific exceptions. 
# In this case, we are handling the ValueError exception, which occurs when the input cannot be converted to an integer.
    print("That is not a valid number!")

# print(f"You entered: {x}")
# If the user enters a valid number, it will be printed. If the user enters an invalid number, the except block will be executed and an error message will be printed.
# The error message here will be the NameError, because the variable x is not defined in the except block. This is because the variable x is only defined in the try block, and if an exception occurs, the code in the try block is not executed, so x is never defined.

# Instead, we can use an else block to handle the case where no exceptions occur. The else block will only be executed if the try block does not raise an exception.
else:
    print(f"You entered: {x}")


# We can loop this code to keep asking the user for input until they enter a valid number. We can use a while loop for this.

while True:
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("That is not a valid number!")
        # OR 
        #pass
        # The pass statement is used to indicate that we want to do nothing in the except block. This is useful when we want to handle an exception but do not want to take any specific action.
    else:
        break

print(f"You entered: {x}")



# Problem Set:

# Fuel Gauge:
# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# Implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

x = y = 0

while True:
    try:
        fuelFraction = input("Fraction: ")
        fuelFraction = fuelFraction.split("/")
        x, y = int(fuelFraction[0]), int(fuelFraction[1])

        if x > y or x < 0:
            continue

        fuelAmount = (x / y) * 100
        break

    except (ValueError, ZeroDivisionError):
        pass


fuelAmount = round(fuelAmount)

if fuelAmount <= 1:
    print("E")
elif fuelAmount >= 99:
    print("F")
else:
    print(f"{fuelAmount}%")


# Felipe's Taqueria:

# Felipe's Taqueria
# One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:
#{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
#}
#In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.




menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order = 0

while True:
    try:
        food = input("Item: ").title()
        if food in menu:
            order = order + float(menu[food])
            print(f"Total: ${order:.2f}")

    except EOFError:
        print()
        break

        

        
# Grocery List:
# Grocery List

Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.


groceryList = {}

while True:
    try:
        item = input().upper()
        if item not in groceryList:
            x = 1
            groceryList[item] = x
        else:
            groceryList[item] = x+1

    except EOFError:
        for key in sorted(groceryList.keys()):
            print(f"{groceryList[key]} {key}")
        break


        
# Outdated

In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.



months = {

    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12

}

while True:

    try:
        dateInput = input("Date: ").strip()

        if "/" in dateInput:

            month, day, year = dateInput.split("/")

            month, day, year = int(month), int(day), int(year)

            if month < 1 or month > 12 or day < 1 or day > 31:

                continue

            else:

                print(f"{year}-{month:02}-{day:02}")

                break

        elif "," in dateInput:

            dateInput = dateInput.replace(",", "")

            month_str, day, year = dateInput.split(" ")

            day, year = int(day), int(year)

            if month_str not in months:

                continue

            elif day < 1 or day > 31:

                continue

            else:

                print(f"{year}-{months[month_str]:02}-{day:02}")

                break

    except ValueError:

        pass

        
"""
