"""Decide whether a guest is a friend or a threat.

This uses a dictionary and a string comparison.
"""

guest = {
    "name": "Vera",
    "mood": "friendly"
}

if guest["mood"] == "friendly":
    print("Vera smiles and shares a secret ritual with the player.")
elif guest["mood"] == "suspicious":
    print("Vera watches the player closely and seems ready to attack.")
else:
    print("Vera is a hidden enemy and the player must run.")
