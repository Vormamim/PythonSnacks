"""A function with a parameter.

This function recommends a record based on the customer genre.
"""


def record_recommendation(genre):
    if genre == "Jazz":
        print("Recommended: Blue Train")
    elif genre == "Rock":
        print("Recommended: Rumours")
    else:
        print("Recommended: Thriller")


record_recommendation("Jazz")
