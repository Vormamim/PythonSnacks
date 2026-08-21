"""A simple nested loop.

This loop runs inside another loop.
"""

for outer in range(1, 3):
    for inner in range(1, 3):
        print(f"outer={outer}, inner={inner}")
