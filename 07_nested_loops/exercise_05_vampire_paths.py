"""Exercise: print vampire paths.

This shows possible paths in a small map.
"""

rooms = ["crypt", "hall", "tower"]
paths = ["left", "right"]

for room in rooms:
    for path in paths:
        print(room, path)
