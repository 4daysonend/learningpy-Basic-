# learning about User input and Command Flow
# to accept user input from the command line; we first must assign the input a variable we are going to use

# ex: value = input('message to the user')
import sys
import random
from enum import Enum

# this is for constant variables that do not change

print("")

# *** NOW I'm going to make the game a function and see how that effec the gameplay.
# *** you can see the function Below in 'def'


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPPER = 2
        SCISSORS = 3


# we removed the while loop to use recursion

    # used alt+z to put code on a newline
    playerchoice = input(
        "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n ")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3. ")
        return play_rps

    player = int(playerchoice)

    # now the computer has to choose and option in game.
    computerchoice = random.choice("123")
    # make this computerchoice a integer
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

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

    print("\n Play again?")

    while True:
        playagain = input("\nY for Yes or \nQ to Quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("BYE!👋👋👋")
        # break


play_rps()
