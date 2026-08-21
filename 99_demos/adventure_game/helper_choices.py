"""A small helper script for a text adventure.

This shows how a game can store choices in a list and then print them.
It is a simple example for beginner programmers.
"""

choices = [
    "Open the castle gate",
    "Walk into the moonlit forest",
    "Enter the crypt",
    "Hide in the tower"
]

print("Choose your next move:")

for choice in choices:
    print("- " + choice)
