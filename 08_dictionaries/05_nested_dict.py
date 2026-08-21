"""A dictionary inside a dictionary.

This is useful when storing more detailed information.
"""

record = {
    "title": "Blue Train",
    "details": {
        "genre": "Jazz",
        "price": 24.00
    }
}

print(record["details"]["genre"])
