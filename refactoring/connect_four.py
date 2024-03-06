import sys

# create empty game board
board = [
         [".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", "."],
]

while True:

    # print the game board
    print()
    print("1 2 3 4 5 6 7")
    for row in board:
        line = ""
        for cell in row:
            line += cell + " "
        print(line)
    print()

    # first player moves
    x = input("enter a column (1-7) ")
    x = int(x)

    # find empty cell closest to bottom
    if board[0][x - 1] == ".":
        y = 0
    if board[1][x - 1] == ".":
        y = 1
    if board[2][x - 1] == ".":
        y = 2
    if board[3][x - 1] == ".":
        y = 3
    if board[4][x - 1] == ".":
        y = 4

    board[y][x - 1] = "X"
    # end: player moves

    # check rows
    for row in board:
        for i in range(4):
            if (
                row[i] == "X"
                and row[i + 1] == "X"
                and row[i + 2] == "X"
                and row[i + 3] == "X"
            ):
                print("Player 1 (X) wins!")
                sys.exit(0)

    # check columns
    for i in range(7):
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X" and board[3][i] == "X":
            print("Player 1 (X) wins!")
            sys.exit(0)
        elif board[1][i] == "X" and board[2][i] == "X" and board[3][i] == "X" and board[4][i] == "X":
            print("Player 1 (X) wins!")
            sys.exit(0)

    # check diagonals
    for y in range(2):
        for x in range(4):
            if (
                board[y][x] == "X"
                and board[y + 1][x + 1] == "X"
                and board[y + 2][x + 2] == "X"
                and board[y + 3][x + 3] == "X"
            ):
                print("Player 1 (X) wins!")
                sys.exit(0)
    for y in range(2):
        for x in range(3, 7):
            if (
                board[y][x] == "X"
                and board[y + 1][x - 1] == "X"
                and board[y + 2][x - 2] == "X"
                and board[y + 3][x - 3] == "X"
            ):
                print("Player 1 (X) wins!")
                sys.exit(0)

    # print the game board
    print()
    print("1 2 3 4 5 6 7")
    for row in board:
        line = ""
        for cell in row:
            line += cell + " "
        print(line)

    print()

    # second player moves
    x = input("enter a column (1-7) ")
    x = int(x)

    # find empty cell closest to bottom
    if board[0][x - 1] == ".":
        y = 0
    if board[1][x - 1] == ".":
        y = 1
    if board[2][x - 1] == ".":
        y = 2
    if board[3][x - 1] == ".":
        y = 3
    if board[4][x - 1] == ".":
        y = 4

    board[y][x - 1] = "O"

    # check rows
    for row in board:
        for i in range(4):
            if (
                row[i] == "O"
                and row[i + 1] == "O"
                and row[i + 2] == "O"
                and row[i + 3] == "O"
            ):
                print("Player 2 (O) wins!")
                sys.exit(0)

    # check columns
    for i in range(7):
        if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O" and board[3][i] == "O":
            print("Player 2 (O) wins!")
            sys.exit(0)
        elif board[1][i] == "O" and board[2][i] == "O" and board[3][i] == "O" and board[4][i] == "O":
            print("Player 2 (O) wins!")
            sys.exit(0)

    # check diagonals
    for y in range(2):
        for x in range(4):
            if (
                board[y][x] == "O"
                and board[y + 1][x + 1] == "O"
                and board[y + 2][x + 2] == "O"
                and board[y + 3][x + 3] == "O"
            ):
                print("Player 2 (O) wins!")
                sys.exit(0)
    for y in range(2):
        for x in range(3, 7):
            if (
                board[y][x] == "O"
                and board[y + 1][x - 1] == "O"
                and board[y + 2][x - 2] == "O"
                and board[y + 3][x - 3] == "O"
            ):
                print("Player 2 (O) wins!")
                sys.exit(0)
