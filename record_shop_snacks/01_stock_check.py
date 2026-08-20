"""Check if a record title is in the shop's stock list.

This script uses a list of record titles and a simple decision.
A beginner can change the names, add more records, or ask for input.
"""

stock = [
    "Abbey Road",
    "Rumours",
    "Kind of Blue",
    "Thriller",
    "Blue Train"
]

wanted_record = "Rumours"

if wanted_record in stock:
    print(f"Yes! '{wanted_record}' is in stock.")
else:
    print(f"Sorry, '{wanted_record}' is not in stock today.")
