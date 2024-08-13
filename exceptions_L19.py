# print(x)
# just trying to print(x) will not work and result in a "NameError:" when the script is ran. NameError is a specific type of EXECPTION.

#  we are going to create our custom expection messages below
class JustNotCoolError(Exception):
    pass


# REMEMBER ***** wrap a try-block around the task you are trying to do then at minimum you'll need 1 except; even if you're just catching each exception as error. If you're expecting some as possibilities it is good to create those.
x = 2
try:
    raise JustNotCoolError("Ayo, that's not p bruh.")
    # raise Exception("I'm a custom exception!")
    # print(x/0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
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
