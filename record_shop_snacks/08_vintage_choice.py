"""Decide whether a record is a vintage item.

The record's year tells us if it should be treated as a vintage find.
This is a simple age-based decision.
"""

record = {
    "title": "Kind of Blue",
    "year": 1959,
    "price": 32.00
}

if record["year"] < 1965:
    print(f"'{record['title']}' is a vintage record and a special find!")
else:
    print(f"'{record['title']}' is newer, but still a great addition to the collection.")
