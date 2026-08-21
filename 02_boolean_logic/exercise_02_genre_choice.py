"""Exercise: choose a recommendation from a list.

This checks whether a genre is available.
"""

genres = ["rock", "dance", "classical"]
choice = "dance"

if choice in genres:
    print("We have a recommendation for you.")
else:
    print("We can suggest something else.")
