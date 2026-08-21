"""Search a dictionary for a price value.

This checks the price for a key.
"""

record = {"title": "Ghost Town", "price": 25}

if "price" in record:
    print(record["price"])
else:
    print("No price found.")
