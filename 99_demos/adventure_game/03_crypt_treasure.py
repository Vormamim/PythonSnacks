"""Decide whether to take a treasure from a vampire crypt.

This script shows a simple danger check using a decision.
"""

treasure = {
    "name": "Moonstone Crown",
    "cursed": True,
    "value": 100
}

if treasure["cursed"]:
    print("The Moonstone Crown is cursed. The player chooses not to take it.")
else:
    print("The Moonstone Crown is safe. The player takes it and leaves the crypt.")
