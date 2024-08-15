import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

file = open("names_L22.txt")
# print(file.read())

# <--- to read the first 4 characters of the file, I'm placing a 4 in the ().
# print(file.read(4))

# read the first line of the file.
# print(file.readline())
# print(file.readline())

# below I'm going to loop through each line of the file.

for line in file:
    print(line)

file.close()

# checks

try:
    file = open("name_list.txt")
    print(file.read())
except:
    print("The file you want to read doesn't exist")
finally:
    file.close()


# Append - creates the file if it doesn't exist

f = open("names_L22.txt", "a")
f.write("\nRob")
f.close()

f = open("names_L22.txt")
print(f.read())
f.close()

# Write (overwrite)

f = open("context_L22.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context_L22.txt")
print(f.read())
f.close()

# two ways to create a new file

# opens a file for writing, creates the file if it does not exist
f = open("name_L22.txt", "w")
f.close()

# creates the specified file, but returns an error if the file exists
if not os.path.exists("myles.txt"):
    f = open("myles.txt", "x")
    f.close()

# Delete a file

# avoid an error if it doesn't exist

if os.path.exists("myles.txt"):
    os.remove("myles.txt")
else:
    print("The file you wish to delete does not exist.")


# this is whats widely used below! USE THIS, it is more concise with the # checks section

with open("more_names_L22.txt") as f:
    content = f.read()

with open("names_L22.txt", "w") as f:
    f.write(content)
