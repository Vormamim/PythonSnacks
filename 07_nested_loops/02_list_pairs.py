"""Print pairs from two lists.

This shows how one list can be combined with another.
"""

genres = ["rock", "jazz"]
prices = [10, 15]

for genre in genres:
    for price in prices:
        print(genre, price)
