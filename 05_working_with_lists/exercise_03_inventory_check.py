"""Exercise: Check whether a player has an item in inventory.

This demonstrates list checking in a game context.
"""

inventory = ["potion", "shield", "map"]
item = "potion"

if item in inventory:
    print("The player has the potion.")
else:
    print("The player does not have the potion.")
