"""
check whether there are four items in a row.
"""

WIN_POSITIONS = []

# rows
for j, row in enumerate(d):
    for i in range(4):
        WIN_POSITIONS.append([(j,i), (j,i+1), (j,i+2), (j,i+3)])

#columns
for i in range(7):
    WIN_POSITIONS.append([(0,i), (1,i), (2,i), (3,i)])
    WIN_POSITIONS.append([(1,i), (2,i), (3,i), (5,i)])

# diagonals
for y in range(2):
    for x in range(4):
        WIN_POSITIONS.append([(y,x), (y+1,x+1), (y+2,x+2), (y+3,x+3)])
    for x in range(3, 7):
        WIN_POSITIONS.append([(y,x), (y+1,x-1), (y+2,x-2), (y+3,x-3)])


def check_positions(d, positions, player):
    """positions = tuple of four x/y positions"""
    contents = [d[y][x] for x, y in positions]
    contents = ''.join(contents)  # e.g. 'XXO.'
    if contents == player * 4:
        return True


def check_winner(d, player):
    for positions in WIN_POSITIONS:
        if check_positions(d, positions, player):
            return True
