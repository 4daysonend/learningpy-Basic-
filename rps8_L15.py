# this is rps would have a commandlineargument ro personalize the game, found at the bottom of the code
import sys
import random
from enum import Enum


def rps(name="Myles"):  # <--- Added in chp 15

    # in RPS4 we are going to add one GLOBAL Variable  to get a better understanding of chapter 11.
    game_count = 0  # <--- global variable added in chapter 11
    player_wins = 0
    python_wins = 0

    print("")

# *** NOW I'm going to make the game a function and see how that effec the gameplay.
# *** you can see the function Below in 'def'
    def play_rps():
        nonlocal name  # <--- Added in chp 15
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPPER = 2
            SCISSORS = 3

    # we removed the while loop to use recursion

        playerchoice = input(
            # <--- modified in chp 15
            f"\n{name}, please enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n ")

        if playerchoice not in ["1", "2", "3"]:
            # <--- modified in chp 15
            print(f"{name}, please enter 1, 2, or 3. ")
            return play_rps()

        player = int(playerchoice)

        # now the computer has to choose and option in game.
        computerchoice = random.choice("123")
        # make this computerchoice a integer
        computer = int(computerchoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )

        def decide_winner(player, computer):  # <---- Added in chapter 11
            # building a controlflow code.
            nonlocal name  # <--- Added in chp 15
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎊 {name}, you Win!"  # <--- modified in chp 15
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎊 {name}, you Win!"  # <--- modified in chp 15
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎊 {name}, you Win!"  # <--- modified in chp 15
            elif player == computer:
                return "😲 Tie Game!"
            else:
                python_wins += 1
                return f"🐍 Python Wins!\nSorry, {name}."

        # <---- Added in chapter 11
        game_result = decide_winner(player, computer)

        print(game_result)  # <---- Added in chapter 11

        nonlocal game_count  # <--- Added for chapter 11 scope
        game_count += 1  # <--- Added for chapter 11 scope}

        print(f"\nGame count:  {game_count}")  # <---- Added in chapter 11
        # <---- Added in chapter 12}
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\n Play again?, {name}?")  # <---- Added in chapter 11

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
            sys.exit(f"BYE {name}!👋👋👋")
            # break

    return play_rps  # <--- this is the closure for the functions


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps()  # <--- close the global function
    rock_paper_scissors()
