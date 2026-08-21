"""Exercise: roll two dice and total the score.

This shows how random numbers can be added together.
"""

import random

roll_1 = random.randint(1, 6)
roll_2 = random.randint(1, 6)

total = roll_1 + roll_2
print("First roll:", roll_1)
print("Second roll:", roll_2)
print("Total:", total)
