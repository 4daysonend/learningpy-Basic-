# functions are reuseable blocks of code.
def hello_world():
    print("Hello World!")


hello_world()


# default perameter: num1=0
# default perameter: num2=0


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
        # <-- this might be more useful if you are using it for mathematical equations.
    return num1 + num2


total = sum(7, 4)
print(total)
print('')


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")

# ** kwargs = key . word . arguments


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Myles", last="Petillo")

print('')

count = 1
print("count to 10")
while count > 0:
    print(f'Count: {count}')
    count += 1
    break
