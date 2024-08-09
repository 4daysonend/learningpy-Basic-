# examples of lists

# first ex is directly below but not limited to...
users = ['Myles', 'Malek', 'Micah']

# this is a valid list
data = ['Myles', '29', 'True']

# also, this ex below.
emptylist = []

# checking this values in the list above.
print("Myles" in users)
print("Myles" in data)
print("Myles" in emptylist)
print('')
print(users[0])
print(users[-2])
print('')
print(users.index('Malek'))
print('')
# if you want the range of value
print(users[0:2])
print(users[1:])
print(users[-3:-1])
print('')
print(len(data))
print('')
# if you want to add to the list
users.append('Camry')
print(users)

users += ['Tyla']
print(users)

users.extend(['Eli', 'Britt'])
print(users)

# users.extend(data)
# print(users)
print('')
users.insert(0, 'Mary')
print(users)

# made place for new additions to the list
users[2:2] = ['Carolyn', 'Candy']
print(users)

# replace things in the list
users[1:3] = ['Sandra', 'Sharon']
print(users)
print('')

# How can you remove things from the list
users.remove('Britt')
print(users)
print('')

# how can you 'pop' off the last item of the list
print(users.pop())
print(users)
print('')

# specifically delete user from list
del users[0]
print(users)

# del data <--- this won't work
data.clear()  # this is how it works
print(data)
print('')

# sorting in python
users.sort()
print(users)
print('')

# <--- not the outcome that is expected did not go to positon 1 or 2 in the list
users[1:2] = ['dave']
users.sort()
print(users)
print('')

users.sort(key=str.lower)  # <-- this had the expected outcome!
print(users)
print('')

# below are some exmaples with numbers in a list

nums = [4, 29, 51, 1, 90]  # <-- supplied the list in reverse
nums.reverse()
print(nums)
print('')

# <-- sorted the list by numeric value and supplied the list greatest number to least
# nums.sort(reverse=True)
# print(nums)
# print('')

print(sorted(nums, reverse=True))  # <-- this is a better way to write a sort
print(nums)
print('')

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()  # <-- from smallest to largest
print(mycopy)
print(nums)
print('')

print(type(nums))
print('')

mylist = list([1, "Myles", True])
print(mylist)
print('')

# Tuples

mytuple = tuple(('Malek', 27, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Malek')
newtuple = tuple(newlist)
print(newtuple)
print('')

# unpacking a tuple
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

# this will count howmany occurances the number 2 has in the tuple
print(anothertuple.count(2))

print('')
