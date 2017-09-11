"""
create empty 6x6 nested list
"""

table = []
for i in range(6):
    row = [0] * 6
    table.append(row)

print(table)
