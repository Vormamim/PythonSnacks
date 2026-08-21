"""Find a record in a list of dictionaries.

This looks for a matching title.
"""

records = [
    {"title": "Moonlight", "price": 12},
    {"title": "Velvet Sky", "price": 15},
    {"title": "Night Echo", "price": 18}
]

search_title = "Velvet Sky"

for record in records:
    if record["title"] == search_title:
        print(record["price"])
