"""Exercise: check a record dictionary.

This uses a dictionary value in a decision.
"""

record = {
    "title": "Abbey Road",
    "price": 22.00,
    "in_stock": True
}

if record["in_stock"]:
    print("The record is in stock.")
else:
    print("The record is not in stock.")
