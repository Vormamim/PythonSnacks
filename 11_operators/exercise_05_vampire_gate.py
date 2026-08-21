"""Exercise: use or and not in a vampire gate check.

The gate opens if the player is invited or the vampire is not nearby.
"""

invited = False
vampire_nearby = False

if invited or not vampire_nearby:
    print("The gate opens.")
else:
    print("The gate stays shut.")
