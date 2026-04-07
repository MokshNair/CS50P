"""
Lecture 4: Libraries

Libraries are collections of pre-written code that can be imported and used in your own programs. They provide a way to reuse code and save time by not having to write everything from scratch.



# Random Library:
import random

coin = random.choice(["heads", "tails"])

print(coin)
# This will print either "heads" or "tails" randomly each time you run the program.

# Another function from the random library is randint, which generates a random integer between two specified values. For example:

random_number = random.randint(1, 10)

print(random_number)
# This will print a random integer between 1 and 10 (inclusive) each time you run the program.

# Yet another function from the random library is shuffle, which randomly shuffles the elements of a list. For example:

my_list = [1, 2, 3, 4, 5]

random.shuffle(my_list)

print(my_list)
# This will print the list in a random order each time you run the program.


# Statistics Library:
import statistics

print(statistics.mean([1, 2, 3, 4, 5]))  # This will print the mean of the list, which is 3.0


# Sys Library:
import sys

print("hello, my name is", sys.argv[1]) # argv stands for "argument vector" and is a list that contains the command-line arguments passed to the program. The first element (sys.argv[0]) is the name of the script itself, and the subsequent elements (sys.argv[1], sys.argv[2], etc.) are the additional arguments passed to the program. In this case, sys.argv[1] refers to the first command-line argument passed to the program, which is expected to be a name.
# This will print "hello, my name is" followed by the first command-line argument passed to the program. For example, if you run the program with "python script.py Moksh", it will print "hello, my name is Moksh".



# APIs, Requests, and JSON:

import json
# JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is commonly used for transmitting data in web applications.
import requests
# This is a library that allows you to send HTTP requests and interact with APIs (Application Programming Interfaces). It provides functions for making GET, POST, PUT, DELETE, and other types of HTTP requests.
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    f"https://itunes.apple.com/search?entity=song&limit=15&term={sys.argv[1]}")

o = response.json()
for result in o["results"]:
    print(result["trackName"])
# This code sends a GET request to the iTunes Search API, searching for a song based on the command-line argument provided. It then parses the JSON response and prints the name of the track found in the search results.
"""

"""


# Problem Set 4: Libraries


# Emojize:

# Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby you can type, for instance, :thumbs_up:, which will be automatically converted to 👍. Some programs additionally support aliases, whereby you can more succinctly type, for instance, :thumbsup:, which will also be automatically converted to 👍.

# See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.

# In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.

import emoji

emojiInput = input("Input: ")

print("Output: " + emoji.emojize(emojiInput, language='alias'))

"""

"""

# Frank, Ian and Glen’s Letters:

FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art.
Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.


import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

availableFonts = figlet.getFonts()

if len(sys.argv) == 1:

    UserInput = input("Input: ")
    figlet.setFont(font=random.choice(availableFonts))
    print(figlet.renderText(UserInput))

elif len(sys.argv) == 3:

    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in availableFonts):

        UserFont = sys.argv[2]
        UserInput = input("Input: ")
        figlet.setFont(font=UserFont)
        print(figlet.renderText(UserInput))

    else:

        sys.exit("Invalid usage")

else:

    sys.exit("Invalid usage")

    
"""

"""

# Adieu, Adieu

In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

Adieu, adieu, to yieu and yieu and yieu
Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu
To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 𝑛 names with 𝑛 −1commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl



import inflect

p = inflect.engine()
ListOfNames = []

while True:

    try:
        name = input("Name: ")
        ListOfNames.append(name)

    except EOFError:
        print()
        break

FormattedNames = p.join(ListOfNames)

print(f"Adieu, adieu, to {FormattedNames}")

"""

"""
# Guessing Game

Implement a program that:

Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.



import random as r

while True:

    try:
        Level = input("Level: ")
        levelVal = int(Level)
        if levelVal > 0:
            break

    except ValueError:
        continue


randomNum = r.randint(1,levelVal)

while True:

    try:
        guess = input("Guess: ")
        guessVal = int(guess)

        if guessVal <= 0:
            continue

        elif guessVal < randomNum:
            print("Too small!")

        elif guessVal > randomNum:
            print("Too large!")

        elif guessVal == randomNum:
            print("Just right!")
            break


    except ValueError:
        continue

"""

"""
# Little Professor

In a file called professor.py, implement a program that:

Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. No need to support operations other than addition (+).
Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()



# SOLUTION:

import random

def main():

    Level = get_level()

    score = 0

    for _ in range(10):

        x = generate_integer(Level)
        y = generate_integer(Level)

        Answer = x + y
        tries = 0

        while tries < 3 :

            try:
                UserAnswer = int(input(f"{x} + {y} = "))

                if UserAnswer == Answer:

                    score = score + 1
                    break


                else:

                    print("EEE")
                    tries = tries + 1

            except ValueError:

                print("EEE")
                tries = tries + 1


        if tries == 3:

            print(f"{x} + {y} = {Answer}")

    print(f"Score: {score}")

def get_level():

    while True:

        try:

            level = int(input("Level: "))

            if level not in range(1,4):

                continue

            return level

        except ValueError:
            continue

def generate_integer(level):

    if level not in [1,2,3]:

        raise ValueError

    if level == 1:

        randomNo = random.randint(0,9)
        return randomNo

    elif level == 2:

        randomNo = random.randint(10,99)
        return randomNo

    elif level == 3:

        randomNo = random.randint(100,999)
        return randomNo


if __name__ == "__main__":
    main()

"""

"""

# Bitcoin Price Index

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. 

Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.

import sys

import requests

if len(sys.argv) == 1:

    sys.exit("Missing command-line argument")

try:

    btc = float(sys.argv[1])

except ValueError:
     sys.exit("Command-line argument is not a number")
     

try:

    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=88f8f77195a4a0a6529521b5a3024f562f99c098e60383777b0aff9a507b648d")

except requests.RequestException:

    sys.exit("Error fetching data from CoinCap")

data = response.json()
price = float(data["data"]["priceUsd"])

totalPrice = price * btc
print(f"${totalPrice:,.4f}")

"""