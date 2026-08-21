"""A function returns the total of an inventory.

This adds up the values in a list and returns the total.
"""


def total_inventory(items):
    total = 0
    for item in items:
        total = total + item
    return total


print(total_inventory([2, 3, 5]))
