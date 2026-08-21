"""Check whether a key exists in a dictionary.

This uses the `in` operator.
"""

vampire = {
    "name": "Luna",
    "mood": "calm"
}

if "name" in vampire:
    print("The key exists.")
else:
    print("The key does not exist.")
