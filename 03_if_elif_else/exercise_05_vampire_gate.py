"""Exercise: Choose a gate in a vampire castle.

This uses a decision chain to decide what happens next.
"""

gate = "black gate"

if gate == "moon gate":
    print("The courtyard is glowing and safe.")
elif gate == "iron gate":
    print("The gate is heavy and dangerous.")
elif gate == "black gate":
    print("The black gate opens to a secret crypt.")
else:
    print("A hidden passage appears under the stairs.")
