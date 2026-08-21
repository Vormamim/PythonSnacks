"""Exercise: find duplicates in a list.

This checks whether the same item appears more than once.
"""

items = ["apple", "banana", "apple", "grape"]

if items.count("apple") > 1:
    print("There is a duplicate apple in the list.")
else:
    print("No duplicates found.")
