"""Choose a gate at the vampire castle.

The player picks a gate and the story changes depending on the choice.
This is a simple example of making a decision in Python.
"""

player = {
    "name": "Ari",
    "gate_choice": "moon gate"
}

if player["gate_choice"] == "moon gate":
    print("Ari opens the moon gate and steps into a silver-lit courtyard.")
elif player["gate_choice"] == "iron gate":
    print("Ari bangs the heavy iron gate and hears a warning growl from inside.")
else:
    print("Ari chooses the hidden door and discovers a secret passage under the castle.")
