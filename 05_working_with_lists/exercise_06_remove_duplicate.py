"""Exercise: Check for duplicates in a list.

This is a simple example of using values in a list to make a decision.
"""

items = ["apple", "banana", "apple", "grape"]

if items.count("apple") > 1:
    print("There is a duplicate apple in the list.")
else:
    print("No duplicate apple found.")
