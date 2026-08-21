"""Decide the type of blood a vampire chooses.

This script uses a dictionary and a decision chain.
"""

vampire = {
    "name": "Luna",
    "blood_type": "rose"
}

if vampire["blood_type"] == "rose":
    print("Luna chooses rose blood. It is rare and very calming.")
elif vampire["blood_type"] == "ruby":
    print("Luna chooses ruby blood. It is rich and full of power.")
elif vampire["blood_type"] == "midnight":
    print("Luna chooses midnight blood. It is dark and mysterious.")
else:
    print("Luna chooses a hidden blood type and disappears into the shadows.")
