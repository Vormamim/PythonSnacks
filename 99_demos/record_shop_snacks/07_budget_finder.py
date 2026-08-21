"""Find records that fit within a customer's budget.

This uses a list of record dictionaries. The script checks price against a budget.
It prints the records that are affordable.
"""

records = [
    {"title": "Rumours", "price": 18.50},
    {"title": "Blue Train", "price": 24.00},
    {"title": "The Miseducation", "price": 19.00},
    {"title": "Abbey Road", "price": 26.00},
    {"title": "Thriller", "price": 16.00}
]

budget = 20.00

print(f"Records under ${budget:.2f}:")

for record in records:
    if record["price"] <= budget:
        print(f"- {record['title']} costs ${record['price']:.2f}")
    else:
        print(f"- {record['title']} is too expensive for this budget.")
