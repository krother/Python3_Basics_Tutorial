"""
Gib die häufigsten Babynamen aus
"""

SCHWELLENWERT = 10000

for line in open('names/yob2014.txt'):
    spalten = line.strip().split(',')
    name = spalten[0]
    anzahl = int(spalten[2])
    if anzahl >= SCHWELLENWERT:
        print("{:20s}{:10d}".format(name, anzahl))
