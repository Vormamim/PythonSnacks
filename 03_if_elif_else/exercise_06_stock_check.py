"""Exercise: Decide whether an item is in stock.

This uses membership testing with a list.
"""

stock = ["vinyl", "cassette", "cd", "turntable"]
item = "cassette"

if item in stock:
    print("Yes, it is in stock.")
elif item == "record":
    print("This item is special and can be ordered.")
else:
    print("No, it is not in stock.")
