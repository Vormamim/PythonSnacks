"""Exercise: compare product prices in a grid.

This shows nested loops being used with simple budget checks.
"""

items = ["record", "book"]
prices = [12, 25]

for item in items:
    for price in prices:
        if price < 20:
            print(item, "is cheap at", price)
        else:
            print(item, "is more expensive at", price)
