"""Check if a value is inside a list.

This shows how to use membership testing in an if statement.
"""

stock = ["vinyl", "cassette", "cd", "turntable"]
item = "vinyl"

if item in stock:
    print("The item is available.")
else:
    print("The item is not available.")
