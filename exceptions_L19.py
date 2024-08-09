# print(x)
# just trying to print(x) will not work and result in a "NameError:" when the script is ran. NameError is a specific type of EXECPTION.

#  we are going to create our custom expection messages below
x = 2
try:
    print(x/0)
except NameError:
    print('NameError means something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error:
    print(error)
else:
    print('No Errors!')
finally:
    print("I'm going to print with or without an error.")
