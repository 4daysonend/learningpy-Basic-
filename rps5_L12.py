
import sys
import random
from enum import Enum


def rps():  # <--- Added in chp 12 closure

    # in RPS4 we are going to add one GLOBAL Variable  to get a better understanding of chapter 11.
    game_count = 0  # <--- global variable added in chapter 11
    player_wins = 0
    python_wins = 0

    print("")

# *** NOW I'm going to make the game a function and see how that effec the gameplay.
# *** you can see the function Below in 'def'
    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPPER = 2
            SCISSORS = 3

    # we removed the while loop to use recursion

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

        def decide_winner(player, computer):  # <---- Added in chapter 11
            # building a controlflow code.
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎊 You Win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎊 You Win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎊 You Win!"
            elif player == computer:
                return "😲 Tie Game!"
            else:
                python_wins += 1
                return "🐍 Python Wins!"

        # <---- Added in chapter 11
        game_result = decide_winner(player, computer)

        print(game_result)  # <---- Added in chapter 11

        nonlocal game_count  # <--- Added for chapter 11 scope
        game_count += 1  # <--- Added for chapter 11 scope

        print("\nGame count: " + str(game_count))  # <---- Added in chapter 11
        # <---- Added in chapter 12
        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))

        print("\n Play again?")  # <---- Added in chapter 11

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

    return play_rps  # <--- this is the closure for the functions


play = rps()  # <--- close the global function

play()


# we've implimented closure to keep track of these game counts and wins without actually creating a Global variable
# learned how to use closure at two different levels using nested functions
