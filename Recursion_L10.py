# Recursion is when a function calls it\'s self
# below is a recursive function
# define add_one with one parameter (num); when I call it with the argument we pass in it will be a number; inside the function, if the number is greater than or eqaul to the number 9 return (end the function) num +1. ADD and new VARIABLE called 'total'
def add_one(num):
    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)
    # ^^^ this ONLY happens when the number is less than 9
    # ^^^ this is the recursive call to the function; it calls itself until its >= 9
    # ^^^ this is just the definition


# add_one(0) # <-- this won\'t print 10 because there isn\'t a print('10') under return num + 1
mynewtotoal = add_one(0)
print(mynewtotoal)
