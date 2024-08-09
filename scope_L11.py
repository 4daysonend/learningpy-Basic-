# this is an example of a 'GLOBAL SCOPE'
name = "Dave"
count = 1
# the parameter (name) is different because it refferring to the function is a 'LOCAL SCOPE'


def another():  # <------ this is a parent function that is being defined in the Global Scope

    color = "blue"  # <---- begining of the local scope
    global count
    count += 1
    print(count)

    def greeting(name):  # <- this is a nested function.
        nonlocal color
        color = "red"
        print(color)  # <----|_____ this indicate the local scope of greeting.
        print(name)  # <----|

    greeting("Dave")


another()
