"""Exercise: Check what a vampire carries.

This uses a list to decide if an item is present.
"""

gear = ["cloak", "dagger", "coin", "map"]

if "cloak" in gear and "dagger" in gear:
    print("The vampire is ready for the journey.")
else:
    print("The vampire still needs equipment.")
