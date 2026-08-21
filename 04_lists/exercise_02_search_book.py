"""Exercise: search for a book in a list.

This uses the `in` operator to test membership.
"""

books = ["The Hobbit", "Matilda", "The Secret Garden"]

book = "Matilda"

if book in books:
    print(f"{book} is in the list.")
else:
    print(f"{book} is not in the list.")
