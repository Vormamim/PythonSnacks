"""Recommend a record based on a customer's favourite genre.

The script makes a decision using an if/elif/else chain.
This helps students see how different choices can lead to different results.
"""

customer = {
    "name": "Mia",
    "favourite_genre": "Jazz"
}

if customer["favourite_genre"] == "Jazz":
    recommendation = "Blue Train"
elif customer["favourite_genre"] == "Rock":
    recommendation = "Rumours"
elif customer["favourite_genre"] == "Soul":
    recommendation = "The Miseducation"
else:
    recommendation = "Thriller"

print(f"{customer['name']}, we recommend '{recommendation}' for you.")
