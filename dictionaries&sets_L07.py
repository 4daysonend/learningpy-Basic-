# Dictionaries: store data vaules in key value pairs
print('')
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

# constructor function
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print('')
print(type(band))
print(len(band))
print('')

# access items in a dictionary
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())
print('')

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)
print('')

# Remove items
print(band.pop("bass"))
print(band)
print('')

# add to the dictionary
band["drums"] = "Bonham"
print(band)

print(band.popitem())  # Going to return a tuple
print(band)
print('')

# Delete and Clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2
print('')

# copy dictionaires
# band2 = band  # create a  reference
# print("Bad copy!")
# print(band2)
# print(band)
# print('')
# band2["drums"] = "Myles"
# print(band)
# print(band2)
# ^ this is NOT best practice when it comes to copying a dictionary it will not

band2 = band.copy()
band2["drums"] = "Myles"
print("Good Copy!")
print(band)
print(band2)
print('')

# or use the dict() constructor function
band3 = dict(band)
print("Good Copy!")
print(band3)
print('')

# Nested dictionaries

member1 = {
    "name": "Myles",
    "instrument": "Vocal"
}
member2 = {
    "name": "Page",
    "instrument": "Drums"
}
band = {
    "member1": member1,
    "mamber2": member2
}
print(band)
# drill down into the nessted dictionary and find a specfic piece of the dictionary
print(band["member1"]["name"])

# Sets data type
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))
print('')

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)
print('')
# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)
print('')

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and dictionaries, too.

# Merge two sets to create a new
one = {1, 2, 3}
two = {4, 5, 6}

# now to merge in py is union
mynewset = one.union(two)
print(mynewset)
print('')

# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)
print('')

# keep everything execpt the ducplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
print('')

# keep exploring the dictionaries and sets groups
