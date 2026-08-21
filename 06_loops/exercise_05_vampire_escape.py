"""Exercise: repeat a message until the escape is successful.

This uses a while loop to keep going until a condition is true.
"""

attempts = 0

while attempts < 3:
    print("The vampire is trying to escape the castle.")
    attempts = attempts + 1

print("The escape attempt is over.")
