
import sys
from checker import check_winner

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


won = False
while not won:
    for player in [P1_PIECE, P2_PIECE]:
        print_playing_field(d)
        x = int(input("enter a column (1-7) "))
        y = find_empty_cell(d)
        d[y][x-1] = player
        won = check_winner(d, player)
        if won:
            print(f'Player {player} wins!')
            break
