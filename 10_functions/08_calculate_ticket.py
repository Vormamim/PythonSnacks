"""A function that returns a ticket price.

This function calculates a ticket cost using a number.
"""


def calculate_ticket(age):
    if age < 18:
        return 5
    return 12


print(calculate_ticket(15))
