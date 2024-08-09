# Closure is a function having access to the scope of its parent function after the parent function has returned.

def parent_function(person, coins):
    # coins = 3

    # <--- play_game [FUNCTION] has access to coins = 3 [PARENT FUNCTION]
    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game  # <--- this is what a Closure is


tommy = parent_function("Tommy", 3)
camry = parent_function("Camry", 5)

tommy()
tommy()

camry()

tommy()

print()
