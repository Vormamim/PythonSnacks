"""Apply a discount to members of the record shop.

This script uses a dictionary for customer data and a simple decision.
A member gets a discount, while a non-member pays full price.
"""

customer = {
    "name": "Sam",
    "member": True,
    "total": 40.00
}

if customer["member"]:
    discount = 10.00
    final_total = customer["total"] - discount
    print(f"{customer['name']} is a member. A $10 discount has been applied.")
    print(f"New total: ${final_total:.2f}")
else:
    print(f"{customer['name']} is not a member. Full price is ${customer['total']:.2f}.")
