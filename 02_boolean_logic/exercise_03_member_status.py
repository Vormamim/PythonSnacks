"""Exercise: decide membership access.

This uses booleans and if statements.
"""

is_member = False
has_ticket = True

if is_member and has_ticket:
    print("You can enter the event.")
elif is_member:
    print("You are a member, but you need a ticket.")
else:
    print("You need to buy a ticket or join first.")
