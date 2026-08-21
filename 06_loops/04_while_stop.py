"""Stop a while loop when a value reaches a limit.

This shows a simple loop control pattern.
"""

money = 0

while money < 5:
    print(f"You have ${money}.")
    money = money + 1

print("You reached the target.")
