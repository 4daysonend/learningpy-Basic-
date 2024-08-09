import sys
from rps9_L16 import rps
from guess_number_L16 import guess


def play_game(name='PLayerOne'):
    # <-- we are defining this value as false (it is a BOOlEAN value), below is a while loop that gives a 'welcome back' message when we come back from anyone of those games.
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playerchoice = input(
            f"\nPlease choose a game: \n1 = Rock Paper Scissors,\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade\n\n"
        )

        if playerchoice not in ["1", "2", "x"]:
            print(f"{name}, please enter 1, 2, or x. ")
            return play_game(name)

        welcome_back = True  # <--- this below is a conditional if/else

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = guess(name)
            guess_my_number()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}!👋")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcarde! 🕹🕹")

    play_game(args.name)
