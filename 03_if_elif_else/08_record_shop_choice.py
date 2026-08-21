"""A record-shop themed decision example.

This shows how a branch can depend on a chosen value.
"""

genre = "Jazz"

if genre == "Jazz":
    print("Recommended: Blue Train")
elif genre == "Rock":
    print("Recommended: Rumours")
else:
    print("Recommended: Thriller")
