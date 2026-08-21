"""A second simple Collector board demo.

This version shows the board more clearly and gives a player
more room to experiment with a few moves.
"""

board = [
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."],
]

print("=== Collector Board Demo ===")
print("Rows and columns go from 0 to 3.")
print("X = your mark")
print("* = removed empty square")
print()

for move in range(1, 7):
    print("Move", move)
    row = int(input("Choose a row: "))
    col = int(input("Choose a column: "))

    if row < 0 or row > 3 or col < 0 or col > 3:
        print("Invalid position.")
        continue

    if board[row][col] != ".":
        print("That square is already used.")
        continue

    board[row][col] = "X"
    print("Your mark is placed.")

    remove_row = int(input("Choose a neighboring empty square to remove: "))
    remove_col = int(input("Choose its column: "))

    if remove_row < 0 or remove_row > 3 or remove_col < 0 or remove_col > 3:
        print("Invalid removal spot.")
        board[row][col] = "."
        continue

    if remove_row == row and remove_col == col:
        print("You cannot remove the square you just marked.")
        board[row][col] = "."
        continue

    if board[remove_row][remove_col] != ".":
        print("Only empty squares can be removed.")
        board[row][col] = "."
        continue

    if abs(remove_row - row) > 1 or abs(remove_col - col) > 1:
        print("That square is not next to your mark.")
        board[row][col] = "."
        continue

    board[remove_row][remove_col] = "*"
    print("The empty square was removed.")
    print()

    for line in board:
        print(line)
    print()

print("The demo is over.")
print("This can be turned into a full collector game later.")
