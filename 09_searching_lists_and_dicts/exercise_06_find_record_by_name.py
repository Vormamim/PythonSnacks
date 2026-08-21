"""Exercise: search a list of records by name.

This finds a matching record title.
"""

records = [
    {"title": "Echoes", "price": 10},
    {"title": "Wolves", "price": 16}
]

for record in records:
    if record["title"] == "Wolves":
        print(record["price"])
