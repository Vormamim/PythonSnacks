"""A simple multiplication table using nested loops.

This prints the times table for 1 to 3.
"""

for first in [1, 2, 3]:
    for second in [1, 2, 3]:
        print(first, "x", second, "=", first * second)
