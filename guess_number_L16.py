# this is Guess My Number a student challenge to understand the chapter that came before.
import sys
import random


def guess(name="Myles"):

    game_count = 0
    player_wins = 0

    def play_gmn():
        nonlocal name  # <--- Added in chp 15
        nonlocal player_wins

        playerchoice = input(
            f"\n{name}, I\n'm thinking of a number 1-3, is it...\n1 ,\n2 , or \n3 \n\n ")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3. ")
            return play_gmn()

        # now the computer has to choose and option in game.
        computerchoice = random.choice("123")

        print(f"\n{name}, you chose {playerchoice}.")
        print(
            f"I was thinking about the number {computerchoice}.\n"
        )
        # make this playerchoice and computerchoice a integer
        player = int(playerchoice)
        computer = int(computerchoice)

        def decide_winner(player, computer):
            # building a controlflow code.
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"🎊 {name}, you Win!"
            else:
                return f"Sorry, {name}. Better luck next time. :"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count:  {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning precentage: {player_wins/game_count:.2%}")

        print(f"\n Play again?, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit \n\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_gmn()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":  # <--- because we want the game to run on its own we are placing this here
                sys.exit(f"BYE {name}!👋👋👋")
            else:
                return

    return play_gmn  # <--- this is the closure for the functions


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

    guess_my_number = guess(args.name)  # <--- close the global function
    guess_my_number()
