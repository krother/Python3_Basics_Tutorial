
import sys

# create empty playing field
d = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]

P1_PIECE = 'X'
P2_PIECE = 'O'


def print_playing_field(d):
    """print the playing field"""
    print()
    print("1 2 3 4 5 6 7")
    for row in d:
        line = ""
        for cell in row:
            line += cell + " "
        print(line)
    print()


while True:
    print_playing_field(d)

    # first player moves
    x = input("enter a column (1-7) ")
    x = int(x)

    # find empty cell closest to bottom
    for i in range(5):
        if d[i][x-1] == '.':
            y = i

    d[y][x-1] = P1_PIECE

    # check rows
    for row in d:
        for i in range(4):
            if row[i] == P1_PIECE and row[i+1] == P1_PIECE \
                and row[i+2] == P1_PIECE and row[i+3] == P1_PIECE:
                    print('Player 1 (X) wins!')
                    sys.exit(0)

    # check columns
    for i in range(7):
        if d[0][i] == P1_PIECE and d[1][i] == P1_PIECE \
            and d[2][i] == P1_PIECE and d[3][i] == P1_PIECE:
                print('Player 1 (X) wins!')
                sys.exit(0)
        elif d[1][i] == P1_PIECE and d[2][i] == P1_PIECE \
            and d[3][i] == P1_PIECE and d[4][i] == P1_PIECE:
                print('Player 1 (X) wins!')
                sys.exit(0)

    # check diagonals
    for y in range(2):
        for x in range(4):
            if d[y][x] == P1_PIECE and d[y+1][x+1] == P1_PIECE \
                and d[y+2][x+2] == P1_PIECE and d[y+3][x+3] == P1_PIECE:
                    print('Player 1 (X) wins!')
                    sys.exit(0)
    for y in range(2):
        for x in range(3, 7):
            if d[y][x] == P1_PIECE and d[y+1][x-1] == P1_PIECE \
                and d[y+2][x-2] == P1_PIECE and d[y+3][x-3] == P1_PIECE:
                    print('Player 1 (X) wins!')
                    sys.exit(0)

    print_playing_field(d)

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

    d[y][x-1] = P2_PIECE

    # check rows
    for row in d:
        for i in range(4):
            if row[i] == P2_PIECE and row[i+1] == P2_PIECE \
                and row[i+2] == P2_PIECE and row[i+3] == P2_PIECE:
                    print('Player 2 (O) wins!')
                    sys.exit(0)

    # check columns
    for i in range(7):
        if d[0][i] == P2_PIECE and d[1][i] == P2_PIECE \
            and d[2][i] == P2_PIECE and d[3][i] == P2_PIECE:
                print('Player 2 (O) wins!')
                sys.exit(0)
        elif d[1][i] == P2_PIECE and d[2][i] == P2_PIECE \
            and d[3][i] == P2_PIECE and d[4][i] == P2_PIECE:
                print('Player 2 (O) wins!')
                sys.exit(0)

    # check diagonals
    for y in range(2):
        for x in range(4):
            if d[y][x] == P2_PIECE and d[y+1][x+1] == P2_PIECE \
                and d[y+2][x+2] == P2_PIECE and d[y+3][x+3] == P2_PIECE:
                    print('Player 2 (O) wins!')
                    sys.exit(0)
    for y in range(2):
        for x in range(3, 7):
            if d[y][x] == P2_PIECE and d[y+1][x-1] == P2_PIECE \
                and d[y+2][x-2] == P2_PIECE and d[y+3][x-3] == P2_PIECE:
                    print('Player 2 (O) wins!')
                    sys.exit(0)
