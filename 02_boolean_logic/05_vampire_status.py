"""Decide a vampire status using boolean logic.

This shows how conditions can be combined.
"""

is_night = True
has_blood = False

if is_night and has_blood:
    print("The vampire is ready.")
elif is_night:
    print("The vampire is hungry.")
else:
    print("The vampire is resting.")
