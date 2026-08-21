"""Exercise: Search for a record title.

This uses a list of record names and a condition.
"""

records = ["Abbey Road", "Rumours", "Blue Train"]

search = "Rumours"

if search in records:
    print(f"{search} is available in the shop.")
else:
    print(f"{search} is not available.")
