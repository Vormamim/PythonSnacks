"""Exercise: check a player inventory list.

This shows a basic item check using a list.
"""

inventory = ["potion", "shield", "map"]
item = "potion"

if item in inventory:
    print("The player has the potion.")
else:
    print("The player does not have the potion.")
