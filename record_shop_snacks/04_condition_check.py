"""Check the condition of a vinyl record before sale.

We use a dictionary for one record and test the condition.
This is a simple example of decision making for beginners.
"""

record = {
    "title": "Blue Train",
    "condition": "Near Mint",
    "price": 30.00
}

if record["condition"] == "Mint":
    print("This record is in excellent condition and perfect for collectors.")
elif record["condition"] == "Near Mint":
    print("This record is in very good condition.")
else:
    print("This record may have some wear but is still for sale.")
