"""Exercise: search a list and decide if an item is available.

This uses a list and an if/else statement.
"""

records = ["album A", "album B", "album C"]
search = "album D"

if search in records:
    print("The record is available.")
else:
    print("The record is not available.")
