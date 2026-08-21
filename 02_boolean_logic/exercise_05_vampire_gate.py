"""Exercise: decide if a vampire gate opens.

A gate opens only for invited guests or if the vampire is not nearby.
"""

invited = True
vampire_nearby = False

if invited or not vampire_nearby:
    print("The gate opens.")
else:
    print("The gate stays shut.")
