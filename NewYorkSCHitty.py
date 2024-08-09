from random import choice

capital = "Albany"

bird = "Pigeon"

flower = "Rose"

song = "Empire State of Mind"


def randomfunfact():
    funfacts = [
        "deadass is a fact",
        "Oldest Subway: NYC's subway is one of the world's oldest and runs 24/7.",
        "Central Park vs. Pelham Bay Park: Pelham Bay Park is three times larger than Central Park.",
        "Languages: Over 800 languages are spoken in NYC.",
        "Statue of Liberty: A gift from France in 1886, designed by Bartholdi and Eiffel."
    ]

    index = choice("01234")

    print(funfacts[int(index)])


# this function will only be called into action if __name__ is the __main__ file
if __name__ == "__main__":
    randomfunfact()
