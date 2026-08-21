"""Offer a bundle discount when a customer buys more than one record.

This shows how a decision can depend on the number of items in a list.
"""

basket = [
    "Rumours",
    "Thriller",
    "Blue Train",
    "The Miseducation"
]

if len(basket) >= 3:
    print("Great choice! Buy 3 or more records and get a 15% bundle discount.")
else:
    print("Add a few more records to unlock the bundle discount.")
