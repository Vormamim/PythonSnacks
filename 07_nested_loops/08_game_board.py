"""Make a simple board using nested loops.

This shows how grids can be created in code.
"""

for row in range(1, 3):
    for col in range(1, 4):
        print("[", row, col, "]", end=" ")
    print()
