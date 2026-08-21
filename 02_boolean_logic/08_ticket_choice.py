"""Decide on a ticket choice using a list and conditions.

This shows how lists and booleans can work together.
"""

tickets = ["student", "adult", "vip"]
choice = "vip"

if choice in tickets:
    print("Valid ticket type.")
else:
    print("This ticket is not allowed.")
