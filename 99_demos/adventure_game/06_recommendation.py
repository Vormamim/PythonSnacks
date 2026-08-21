"""Recommend a move based on the player's goal.

This script helps students see how recommendations depend on data.
"""

player = {
    "goal": "escape",
    "energy": 7
}

if player["goal"] == "escape":
    recommendation = "Take the hidden tunnel beneath the tower."
elif player["goal"] == "power":
    recommendation = "Seek the cursed jewel in the crypt."
else:
    recommendation = "Stay in the library and read the ancient spells."

print(f"Player goal: {player['goal']}")
print(recommendation)
