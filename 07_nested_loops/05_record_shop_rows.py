"""Print rows of record shop items.

This matches each genre with each price.
"""

records = ["rock", "pop"]
prices = [12, 18]

for record in records:
    for price in prices:
        print(record, "costs", price)
