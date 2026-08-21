"""A function with a parameter.

This decides what happens when the player picks a gate.
"""


def vampire_gate(choice):
    if choice == "moon":
        print("The moon gate opens to a silver courtyard.")
    elif choice == "iron":
        print("The iron gate groans and opens slowly.")
    else:
        print("A hidden door swings open beneath the stairs.")


vampire_gate("moon")
