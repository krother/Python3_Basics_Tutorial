"""
Eine einzelne Spalte einer Tabelle ausgeben
"""

data = [
    [ 0,  1,  2,  3],
    [10, 11, 12, 13],
    [20, 21, 22, 23]
    ]

column = []
for row in data:
    column.append(row[2])
print column

    

