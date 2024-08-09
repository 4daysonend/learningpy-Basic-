import math
# string data type

# literal assignment of values

first = "Myles"
last = "Petillo"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string
decade = str(1994)
print(type(decade))
print(decade)

statement = "I like Jazz/Hip-Hop from the " + decade + "s. "
print(statement)

# multiple lines
multiline = '''
Hey, how are you?                                             

I was just checking in.                                        
                                                All good?
'''
print(multiline)

# escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)
# This will show the original length of the multi-line string, it will count every character
print(len(multiline))
# Change the multiline variable to use plus equals (+=)
multiline += "                                          "
multiline = "                                          " + multiline
# check the length function with
print(len(multiline))
# this can be used if you want to remove white space from a file.
print(len(multiline.strip()))
# remove white space from the l-side (left)
print(len(multiline.lstrip()))
# remove white space from the r-side (right)
print(len(multiline.rstrip()))

print("")  # print an empty line

# Building a menu with python
title = "menu".upper()
# print title "menu" with 20 characters of = with "menu" in the middle
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# string index values
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
print(first[-1])
print("")

print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("M"))
print(first.endswith("Z"))

print("")

# Boolean data type
myvalue = True

# constructor function
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

print("")

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# not often used unless you are a electrical engineer
# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)  # real
print(comp_value.imag)  # imaginary

print("")
# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print("")

print(round(gpa))  # round to the nearest integer
print(round(gpa, 1))  # round to the nearest decimal points

print("")

# to complete mathimatical problems using python3
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

print("")

# casting a string to a number
zipcode = "10001"  # string
# changes the string to an integer using the functino int()
zip_value = int(zipcode)
print(type(zip_value))

#  Error will occur when attempting to cast incorrect data
# zip_value = int("New York")
