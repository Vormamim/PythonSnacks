"""Exercise: return the total of a list of record prices.

This function adds the values in a list and returns the total.
"""


def record_total(prices):
    total = 0
    for price in prices:
        total = total + price
    return total


print(record_total([12, 18, 20]))
