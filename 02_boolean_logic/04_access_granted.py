"""Use booleans to decide access.

The customer only gets access if both conditions are true.
"""

is_member = True
age = 20

if is_member and age >= 18:
    print("Access granted.")
else:
    print("Access denied.")
