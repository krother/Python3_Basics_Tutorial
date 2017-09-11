"""
Methode 1 zum Lesen von Textdateien:
- jede Zeile hat die Daten in der gleichen Spalte (Leerzeichen mitgezaehlt)
- einzelne Felder lassen sich durch Stringindizierung ansprechen. 
"""

for line in open('../moviedb/ratings_1000.txt'):
    print (line[11:16])
    print (line[17:])
