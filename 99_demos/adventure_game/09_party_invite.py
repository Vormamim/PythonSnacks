"""Invite guests to a vampire party.

This script uses a list to track invited guests.
It decides whether the party is big enough.
"""

invited = [
    "Sable",
    "Raven",
    "Morrow"
]

if len(invited) >= 3:
    print("The party is lively enough. The vampire host sends out more invitations.")
else:
    print("The party is too small. The host needs a few more guests.")
