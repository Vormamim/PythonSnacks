"""Search a list and print a message.

This is a very simple search using if.
"""

books = ["novel", "poetry", "comic"]

target = "comic"

if target in books:
    print("Found the book.")
else:
    print("Book not found.")
