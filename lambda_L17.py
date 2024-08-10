# lambda function is a single expression that returns a value.
# sometimes reffered to as anonymous functions.
from functools import reduce
def squared(num): return num * num  # <--- this function will square a number
# lambda num : num * num


print(squared(2))


def addTwo(num): return num + 2
# lambda num : num + 2


print(addTwo(12))


def sum_total(a, b): return a + b
# lambda a, b : a + b


print(sum_total(10, 8))

##############################

# lambdas are often used inside of another function, when you really need a quick function that you don't want to save for later.


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

################################
#### Higher-Order functions ####
################################


# Is a function that takes up 1 < functions as arguments of a functino that returns a functions as its result.


numbers = [3, 7, 12, 18, 20, 21]

# <---- much cleaner code than running a while loop
squared_nums = map(lambda num: num * num, numbers)
# map is a function fraction built into python and receives a function as the first argument

print(list(squared_nums))

# map returned the result of the functinon aplied to ech item in our data collection.

################################
# BUILT_IN PY FUNCTION: FILTER #
################################

# lambda num : num % 2 != 0 # <----- it's going to return true or false because we're doing a comparision != using modulous  with % returning the remainer if it is EVEN.

odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

# AGAIN!!! it is a much simpler to have one line of code where you pass in a lambda function and apply it to each item in your data collection that you also pass in to filter just like it was done with MAP.

# filter function filtered out anything that did not get a true result from the function


##############################
# see the top of the file for this High-Order function it requires an import


# lambda acc, curr: acc + curr
# acc = accumilator
# curr = current items
numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)
# there is a more simpler solution to this than whats above.

print(sum(numbers, 10))
# this is above is the simpler solution to reduce in this case.


# ** second example for reduce

# lambda acc, curr: acc + len(curr)

names = ['Myles Petillo', 'Carolyn P', 'Empire State of Mind']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
