"""
Lecture 7 - Regular Expressions

Regular expressions are a powerful tool for matching patterns in text. They allow us to search for specific strings or patterns within a larger body of text.

for example, we can use regular expressions to find all the email addresses in a document, or to validate that a phone number is in the correct format.


# re package
To use regular expressions in Python, we need to import the "re" package. This package provides a set of functions for working with regular expressions.

re.search(pattern, string, flags=0) 
- This function searches for the first occurrence of the pattern in the string and returns a match object if found, or None if not found. for example:

import re

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid email")
else:
    print("Invalid email")

    
# A few examples of regular expression patterns:

. means any character except a newline
* 0 or more repetitions
+ 1 or more repetitions
? 0 or 1 repetition
{m} m repetitions
{m,n} between m and n repetitions

Using this, we can create more complex patterns to match specific types of strings. For example, we can use the following pattern to match a valid email address:

import re

email = input("What's your email? ").strip()

# if re.search(r"..+@.+"backslash"..+", email):
# The r before the string indicates that it is a raw string, which means that backslashes are treated as literal characters and not as escape characters. This allows us to use backslashes in our regular expression without having to escape them. The pattern "..+@.+"backslash"..+" matches any string that contains at least two characters followed by an "@" symbol, followed by at least one character, followed by a "." symbol, and finally followed by at least one character.

    print("Valid email")

else:
    print("Invalid email")


# A few more important symbols in regular expressions:

^ matches the start of a string
$ matches the end of a string or just before the newline at the end of a string
[] matches any single character in brackets
[^] matches any single character not in brackets
[a-z] matches any single character in the range a-z
[A-Z] matches any single character in the range A-Z
[0-9] matches any single digit

This changes our email validation pattern to:


import re

email = input("What's your email? ").strip()
#if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+"backslash".[a-zA-Z0-9._%+-]+$", email):
    print("Valid email")
# The pattern "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+"backslash".[a-zA-Z0-9._%+-]+$" matches any string that starts with one or more characters that are either letters, digits, dots, underscores, percent signs, plus signs, or hyphens, followed by an "@" symbol, followed by one or more characters that are either letters, digits, dots, underscores, percent signs, plus signs, or hyphens, followed by a "." symbol, and finally followed by one or more characters that are either letters, digits, dots, underscores, percent signs, plus signs, or hyphens. This pattern ensures that the email address is in a valid format.
else:
    print("Invalid email")




# Walrus operator

The walrus operator (:=) is a new operator in Python 3.8 that allows us to assign a value to a variable as part of an expression. This can be useful for reducing the number of lines of code and improving readability. For example, we can use the walrus operator to simplify our email validation code:


import re
email = input("What's your email? ").strip()
if (match := re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z0-9._%+-]+$", email)):
# The walrus operator assigns the result of the regular expression search to the variable "match" and also checks if it is truthy (i.e., not None).
    print("Valid email")
else:
    print("Invalid email")
    
"""