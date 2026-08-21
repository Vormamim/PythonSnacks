"""Exercise: match records to prices.

This uses a nested loop to create combinations.
"""

records = ["rock", "pop"]
prices = [10, 20]

for record in records:
    for price in prices:
        print(record, "-", price)
