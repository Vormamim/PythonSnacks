"""Exercise: recommend a record using a dictionary.

This uses values from a dictionary to make a recommendation.
"""

customer = {
    "name": "Sam",
    "favourite_genre": "Jazz"
}

if customer["favourite_genre"] == "Jazz":
    print("Recommended: Blue Train")
else:
    print("Recommended: Thriller")
