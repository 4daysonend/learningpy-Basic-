# for more information on f_strings go to w3schools.com/python/ref_string_format.asp

person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

# this is the %s method of formatting the string

# the %s is where we are going to put the values
message = "\n%s has %s coins left." % (person, coins)
print(message)

# the format method approach
message = "\n{} has {} coins left." .format(person, coins)
print(message)

message = "\n{1} has {0} coins left." .format(coins, person)
print(message)

message = "\n{person} has {coins} coins left." .format(
    coins=coins, person=person
)
print(message)

# dictionary below
player = {'person': 'Dave', 'coins': 3}

message = "\n{person} has {coins} coins left." .format(**player)
print(message)

### * OLD WAY ABOVE*###
######################
# f-Strings! This is th way!

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 * 5} coins left."
print(message)

message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)

message = f"\n{player['person']} has {2 * 5} coins left."
print(message)

######################
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is  {num / 4.52:.2%}")
