
import sys

# create empty playing field
d = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]

while True:
    # print the playing field
    print()
    print("1 2 3 4 5 6 7")
    for row in d:
        line = ""
        for cell in row:
            line += cell + " "
        print(line)

    print()

    # first player moves
    x = input("enter a column (1-7) ")
    x = int(x)

    # find empty cell closest to bottom
    if d[0][x-1] == '.':
        y = 0
    if d[1][x-1] == '.':
        y = 1
    if d[2][x-1] == '.':
        y = 2
    if d[3][x-1] == '.':
        y = 3
    if d[4][x-1] == '.':
        y = 4

    d[y][x-1] = 'X'

    # check rows
    for row in d:
        for i in range(4):
            if row[i] == 'X' and row[i+1] == 'X' \
                and row[i+2] == 'X' and row[i+3] == 'X':
                    print('Player 1 (X) wins!')
                    sys.exit(0)

    # check columns
    for i in range(7):
        if d[0][i] == 'X' and d[1][i] == 'X' \
            and d[2][i] == 'X' and d[3][i] == 'X':
                print('Player 1 (X) wins!')
                sys.exit(0)
        elif d[1][i] == 'X' and d[2][i] == 'X' \
            and d[3][i] == 'X' and d[4][i] == 'X':
                print('Player 1 (X) wins!')
                sys.exit(0)

    # check diagonals
    for y in range(2):
        for x in range(4):
            if d[y][x] == 'X' and d[y+1][x+1] == 'X' \
                and d[y+2][x+2] == 'X' and d[y+3][x+3] == 'X':
                    print('Player 1 (X) wins!')
                    sys.exit(0)
    for y in range(2):
        for x in range(3, 7):
            if d[y][x] == 'X' and d[y+1][x-1] == 'X' \
                and d[y+2][x-2] == 'X' and d[y+3][x-3] == 'X':
                    print('Player 1 (X) wins!')
                    sys.exit(0)

    # print the playing field
    print()
    print("1 2 3 4 5 6 7")
    for row in d:
        line = ""
        for cell in row:
            line += cell + " "
        print(line)

    print()

    # second player moves
    x = input("enter a column (1-7) ")
    x = int(x)

    # find empty cell closest to bottom
    if d[0][x-1] == '.':
        y = 0
    if d[1][x-1] == '.':
        y = 1
    if d[2][x-1] == '.':
        y = 2
    if d[3][x-1] == '.':
        y = 3
    if d[4][x-1] == '.':
        y = 4

    d[y][x-1] = 'O'

    # check rows
    for row in d:
        for i in range(4):
            if row[i] == 'O' and row[i+1] == 'O' \
                and row[i+2] == 'O' and row[i+3] == 'O':
                    print('Player 2 (O) wins!')
                    sys.exit(0)

    # check columns
    for i in range(7):
        if d[0][i] == 'O' and d[1][i] == 'O' \
            and d[2][i] == 'O' and d[3][i] == 'O':
                print('Player 2 (O) wins!')
                sys.exit(0)
        elif d[1][i] == 'O' and d[2][i] == 'O' \
            and d[3][i] == 'O' and d[4][i] == 'O':
                print('Player 2 (O) wins!')
                sys.exit(0)

    # check diagonals
    for y in range(2):
        for x in range(4):
            if d[y][x] == 'O' and d[y+1][x+1] == 'O' \
                and d[y+2][x+2] == 'O' and d[y+3][x+3] == 'O':
                    print('Player 2 (O) wins!')
                    sys.exit(0)
    for y in range(2):
        for x in range(3, 7):
            if d[y][x] == 'O' and d[y+1][x-1] == 'O' \
                and d[y+2][x-2] == 'O' and d[y+3][x-3] == 'O':
                    print('Player 2 (O) wins!')
                    sys.exit(0)
