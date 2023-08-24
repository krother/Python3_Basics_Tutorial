"""
check whether there are four items in a row.
"""
def check_rows(d, player):
    for row in d:
        for i in range(4):
            if row[i] == player and row[i+1] == player \
                and row[i+2] == player and row[i+3] == player:
                    return True


def check_columns(d, player):
    """check columns"""
    for i in range(7):
        if d[0][i] == player and d[1][i] == player \
            and d[2][i] == player and d[3][i] == player:
                return True
        elif d[1][i] == player and d[2][i] == player \
            and d[3][i] == player and d[4][i] == player:
                return True


def check_diagonals(d, player):
    """check diagonals"""
    for y in range(2):
        for x in range(4):
            if d[y][x] == player and d[y+1][x+1] == player \
                and d[y+2][x+2] == player and d[y+3][x+3] == player:
                    return True
    for y in range(2):
        for x in range(3, 7):
            if d[y][x] == player and d[y+1][x-1] == player \
                and d[y+2][x-2] == player and d[y+3][x-3] == player:
                    return True


def check_winner(d, player):
    return check_rows(d, player) or check_columns(d, player) or check_diagonals(d, player)
