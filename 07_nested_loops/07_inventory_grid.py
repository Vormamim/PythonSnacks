"""Create a simple inventory grid.

A nested loop can help display rows of items.
"""

items = ["record", "book", "lantern"]
rows = [1, 2]

for row in rows:
    for item in items:
        print("Row", row, "item", item)
