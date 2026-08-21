"""A simple nested loop.

The inner loop repeats for every outer loop value.
"""

for outer in [1, 2, 3]:
    for inner in ["a", "b"]:
        print(outer, inner)
