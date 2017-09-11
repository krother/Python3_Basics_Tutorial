"""
Sortieren nach mehr als einer Spalte
mit dem Modul operator.
"""

from operator import itemgetter

table = []

# erst einmal die Daten zum Sortieren einlesen
for line in open("spieler_dfb.txt"):
    columns = line.strip().split('\t')
    if len(columns) == 3:
        name = columns[0]
        position = columns[1]
        if columns[2] != '-':
            tore = int(columns[2])
        else:
            tore = None
        table.append([name, position, tore])

# hier findet das eigentliche Sortieren statt
table_sorted = sorted(table, key=itemgetter(1, 2, 0))

for row in table_sorted:
    print (row[1], row[0], row[2])
