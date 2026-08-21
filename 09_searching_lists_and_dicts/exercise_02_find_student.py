"""Exercise: find a student in a list of dictionaries.

This checks each dictionary for a matching name.
"""

students = [
    {"name": "Ava", "grade": "A"},
    {"name": "Ben", "grade": "B"}
]

for student in students:
    if student["name"] == "Ava":
        print(student["grade"])
