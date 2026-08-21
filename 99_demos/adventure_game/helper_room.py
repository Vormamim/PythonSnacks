"""A helper script for describing a game room.

This example shows a room description and a simple decision.
"""

room = {
    "name": "Moonlit Hall",
    "doors": 3,
    "danger_level": "medium"
}

print(f"You are standing in the {room['name']}.")
print(f"There are {room['doors']} doors in the room.")

if room["danger_level"] == "medium":
    print("The air feels tense. One wrong step could be dangerous.")
else:
    print("The room feels calm for now.")
