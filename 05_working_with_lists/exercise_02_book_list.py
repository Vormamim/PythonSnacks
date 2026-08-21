"""Exercise: Check if a book is in a list.

This shows a simple membership check on a list of books.
"""

books = ["The Hobbit", "Matilda", "Charlie and the Chocolate Factory"]

book = "Matilda"

if book in books:
    print(f"{book} is in the list.")
else:
    print(f"{book} is not in the list.")
