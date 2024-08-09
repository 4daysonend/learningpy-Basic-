# module can be considered small code libraries that are based on related features.
# one example of this is the MATH module that contains functions and constant values for use in mathematical equations so we can import math

from math import pi     # these are modules
import sys              # these are modules
import random as rdm    # these are modules with a Alias
from enum import Enum
import NewYorkSCHitty
from rps7_L14 import rock_paper_scissors

print(pi)

print('')
print(NewYorkSCHitty.bird)
NewYorkSCHitty.randomfunfact()
print('')

print(__name__)
print(NewYorkSCHitty.__name__)
# this shows the list of all the options in the module random with the alias rdm
# for item in dir(rdm):
# print(item)

# sys.exit()            # these are modules
# rdm.choice("123")     # these are modules

# <--- how do we find out whats in a module

rock_paper_scissors()
