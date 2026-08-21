"""Exercise: return a recommendation for a vampire choice.

The function decides on a recommendation based on room choice.
"""


def vampire_recommendation(room):
    if room == "crypt":
        return "Take the silver lantern."
    if room == "forest":
        return "Follow the moonlit path."
    return "Stay in the tower and wait."


print(vampire_recommendation("forest"))
