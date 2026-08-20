"""Decide whether a record is within a customer's budget.

The script stores record information in a dictionary and checks the price.
This shows how a decision can be made with an if statement.
"""

record = {
    "title": "Abbey Road",
    "price": 20.00,
    "genre": "Rock"
}

budget = 25.00

if record["price"] <= budget:
    print(f"You can afford '{record['title']}' for ${record['price']:.2f}.")
else:
    print(f"'{record['title']}' costs ${record['price']:.2f}, which is over your budget.")
