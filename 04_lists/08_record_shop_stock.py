"""A record shop stock list.

This example stores record titles and checks if there are enough items.
"""

stock = ["Thriller", "Rumours", "Blue Train", "Kind of Blue"]

if len(stock) >= 4:
    print("The shop has enough records to open for business.")
else:
    print("The shop needs more records.")
