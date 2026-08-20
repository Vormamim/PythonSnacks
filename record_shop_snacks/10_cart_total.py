"""Calculate the total cost of a shopping basket and decide the next step.

This script uses a list of records and a dictionary of prices.
It adds the basket total and uses decisions to give the customer advice.
"""

records = [
    {"title": "Rumours", "price": 18.50},
    {"title": "Thriller", "price": 16.00},
    {"title": "Blue Train", "price": 24.00}
]

customer_budget = 50.00
total = 0.0

for record in records:
    total += record["price"]

print(f"Your basket total is ${total:.2f}.")

if total <= customer_budget:
    print("This is within your budget. You can buy these records.")
elif total <= customer_budget + 10:
    print("You are slightly over budget, but still close. Consider removing one item.")
else:
    print("This basket is over budget. Try a cheaper record or remove one item.")
