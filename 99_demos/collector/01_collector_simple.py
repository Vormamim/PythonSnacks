"""A simple Collector-style board game.

This is a beginner-friendly version.
The board is only 4x4 and the user can play a few turns.
There are no advanced checks or win conditions yet.
"""

board = [
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."],
]

print("Collector - simple version")
print("The board is 4 by 4.")
print("Choose a row and column between 0 and 3.")
print("You place an X and remove one nearby empty square.")
print("Diagonal neighbors are allowed.")
print()

for line in board:
    print(line)
print()

for turn in range(1, 6):
    print("Turn", turn)
    row = int(input("Choose a row: "))
    col = int(input("Choose a column: "))

    if row < 0 or row > 3 or col < 0 or col > 3:
        print("That square is outside the board.")
        continue

    if board[row][col] != ".":
        print("That square is already taken.")
        continue

    board[row][col] = "X"

    print("Choose a nearby empty square to remove.")
    remove_row = int(input("Remove row: "))
    remove_col = int(input("Remove column: "))

    if remove_row < 0 or remove_row > 3 or remove_col < 0 or remove_col > 3:
        print("That square is outside the board.")
        board[row][col] = "."
        continue

    if remove_row == row and remove_col == col:
        print("You cannot remove the square you just marked.")
        board[row][col] = "."
        continue

    row_diff = abs(remove_row - row)
    col_diff = abs(remove_col - col)

    if row_diff > 1 or col_diff > 1:
        print("That square is not a neighboring square.")
        board[row][col] = "."
        continue

    if board[remove_row][remove_col] != ".":
        print("You can only remove an empty square.")
        board[row][col] = "."
        continue

    board[remove_row][remove_col] = "*"
    print("You marked a square and removed a nearby empty one.")
    print()

    for line in board:
        print(line)
    print()

print("Game over.")
print("This is a starter version. You can extend it later with full win checks.")
