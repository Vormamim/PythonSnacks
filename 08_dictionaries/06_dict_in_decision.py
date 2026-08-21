"""Use a dictionary in a decision.

This compares a value from the dictionary to a number.
"""

record = {
    "title": "Thriller",
    "price": 16.00
}

if record["price"] <= 20:
    print("This record is affordable.")
else:
    print("This record is too expensive.")
