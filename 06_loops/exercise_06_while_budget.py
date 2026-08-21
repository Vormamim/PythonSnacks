"""Exercise: spend money until a budget is reached.

This uses a while loop to increase the total until it reaches a limit.
"""

money = 0
budget = 5

while money < budget:
    print(f"Current total: ${money}")
    money = money + 1

print("Budget reached.")
