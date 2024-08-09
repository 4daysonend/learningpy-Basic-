# learning about User input and Command Flow
# to accept user input from the command line; we first must assign the input a variable we are going to use

# ex: value = input('message to the user')
import sys
import random
from enum import Enum

# this is for constant variables that do not change

print("")


class RPS(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSORS = 3


print("")  # empty string
# used alt+z to put code on a newline
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n ")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3. ")

# now the computer has to choose and option in game.
computerchoice = random.choice("123")
# make this computerchoice a integer
computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

# building a controlflow code.
if player == 1 and computer == 3:
    print("🎊 You Win!")
elif player == 2 and computer == 1:
    print("🎊 You Win!")
elif player == 3 and computer == 2:
    print("🎊 You Win!")
elif player == computer:
    print("😲 Tie Game!")
else:
    print("🐍 Python Wins!")
