"""A vampire-themed inventory list.

This example stores items in a list and checks whether a needed item is present.
"""

inventory = ["cloak", "dagger", "blood flask", "map"]

if "blood flask" in inventory:
    print("The vampire has enough supplies for the journey.")
else:
    print("The vampire needs to return to the castle.")
