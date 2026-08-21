"""Exercise: search for a record title.

This is a simple example of searching a list of strings.
"""

records = ["Abbey Road", "Rumours", "Blue Train"]
search = "Rumours"

if search in records:
    print(f"{search} is available.")
else:
    print(f"{search} is not available.")
