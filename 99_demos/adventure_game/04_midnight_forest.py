"""Choose a path in the midnight forest.

The player picks a route and each route leads to a different story outcome.
"""

forest_paths = [
    "silver path",
    "thorn path",
    "misty path"
]

chosen_path = "thorn path"

if chosen_path == "silver path":
    print("The silver path glows and reveals a hidden vampire shrine.")
elif chosen_path == "thorn path":
    print("The thorn path is dangerous, but the player finds a secret diary.")
else:
    print("The misty path leads to a lake where the moon reflects like blood.")
