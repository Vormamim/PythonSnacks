"""Check stock in a record shop using a list.

This shows a list being used in a condition.
"""

stock = ["vinyl", "cassette", "cd"]

if "vinyl" in stock:
    print("Vinyl is in stock.")
elif "cd" in stock:
    print("CDs are available.")
else:
    print("Nothing is in stock.")
