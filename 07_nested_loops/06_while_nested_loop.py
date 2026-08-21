"""A nested while loop example.

This uses one while loop inside another.
"""

row = 1

while row <= 2:
    column = 1
    while column <= 3:
        print("row", row, "column", column)
        column += 1
    row += 1
