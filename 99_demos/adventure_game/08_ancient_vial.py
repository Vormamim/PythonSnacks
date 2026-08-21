"""Check whether a magical vial is safe or cursed.

The script uses a dictionary and several if checks.
"""

vial = {
    "name": "Moonfire Vial",
    "status": "cursed"
}

if vial["status"] == "safe":
    print("The Moonfire Vial glows gently and gives the player strength.")
elif vial["status"] == "cursed":
    print("The vial hisses and a shadow forms around the player.")
else:
    print("The vial is mysterious, but the player cannot tell what it will do.")
