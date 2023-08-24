
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


def find_empty_cell(d):
    """find empty cell closest to bottom"""
    for i in range(5):
        if d[i][x-1] == '.':
            y = i
    return y


def check_rows(d, player):
    for row in d:
        for i in range(4):
            if row[i] == player and row[i+1] == player \
                and row[i+2] == player and row[i+3] == player:
                    print(f'Player {player} wins!')
                    sys.exit(0)


def check_columns(d, player):
    """check columns"""
    for i in range(7):
        if d[0][i] == player and d[1][i] == player \
            and d[2][i] == player and d[3][i] == player:
                print(f'Player {player} wins!')
                sys.exit(0)
        elif d[1][i] == player and d[2][i] == player \
            and d[3][i] == player and d[4][i] == player:
                print(f'Player {player} wins!')
                sys.exit(0)


def check_diagonals(d, player):
    """check diagonals"""
    for y in range(2):
        for x in range(4):
            if d[y][x] == player and d[y+1][x+1] == player \
                and d[y+2][x+2] == player and d[y+3][x+3] == player:
                    print(f'Player {player} wins!')
                    sys.exit(0)
    for y in range(2):
        for x in range(3, 7):
            if d[y][x] == player and d[y+1][x-1] == player \
                and d[y+2][x-2] == player and d[y+3][x-3] == player:
                    print(f'Player {player} wins!')
                    sys.exit(0)


while True:
    print_playing_field(d)

    # first player moves
    x = input("enter a column (1-7) ")
    x = int(x)

    y = find_empty_cell(d)

    d[y][x-1] = P1_PIECE

    check_rows(d, P1_PIECE)
    check_columns(d, P1_PIECE)
    check_diagonals(d, P1_PIECE)

    print_playing_field(d)

    # second player moves
    x = input("enter a column (1-7) ")
    x = int(x)

    y = find_empty_cell(d)

    d[y][x-1] = P2_PIECE

    check_rows(d, P2_PIECE)
    check_columns(d, P2_PIECE)
    check_diagonals(d, P2_PIECE)
