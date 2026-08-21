"""Run a final escape decision for a vampire adventure game.

This script combines a player's health, treasure, and route choice.
"""

player = {
    "health": 5,
    "treasure": 2,
    "route": "tunnel"
}

if player["health"] >= 6 and player["route"] == "tunnel":
    print("The player escapes the castle through the hidden tunnel with treasure.")
elif player["health"] >= 4 and player["treasure"] >= 1:
    print("The player escapes, but is wounded and loses some treasure.")
else:
    print("The player is caught by the castle guards before reaching the gate.")
