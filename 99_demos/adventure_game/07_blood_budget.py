"""Check whether the player has enough blood supplies.

This explores comparing numbers to a target value.
"""

supplies = {
    "blood_packs": 6,
    "needed": 10
}

if supplies["blood_packs"] >= supplies["needed"]:
    print("The player has enough blood supplies for the journey.")
elif supplies["blood_packs"] >= 5:
    print("The player has some supplies, but not enough for a long trip.")
else:
    print("The player is low on blood and should return to the cellar.")
