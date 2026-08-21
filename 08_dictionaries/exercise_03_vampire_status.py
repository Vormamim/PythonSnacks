"""Exercise: store vampire status in a dictionary.

This shows how dictionaries hold related information.
"""

vampire = {
    "name": "Vera",
    "status": "awake",
    "danger": "high"
}

if vampire["danger"] == "high":
    print("Danger level is high.")
else:
    print("Danger level is low.")
