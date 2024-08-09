# this is an example of a while loop
value = "y"
count = 0

while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue

# ^^^ in this loop we are going to increment the count by 1 and print the count so we'll have 1 as the output if count == 5
# ^^^ using the "continue" does have the loop evaluate itself
