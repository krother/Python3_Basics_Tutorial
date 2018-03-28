"""
Namen in eine verschachtelte Liste
(zweidimensionale Liste) einlesen
"""

dateiname = "names/yob1968.txt"

tabelle = []

for zeile in open(dateiname):
    spalten = zeile.strip().split(',')
    name = spalten[0]
    geschlecht = spalten[1]
    anzahl = int(spalten[2])
    eintrag = [name, geschlecht, anzahl]
    tabelle.append(eintrag)

print(tabelle[:5])

# nach Namen in der Tabelle suchen
gesucht = ['John', 'Paul', 'George', 'Ringo']
for eintrag in tabelle:
    if eintrag[0] in gesucht and eintrag[1] == 'M':
        print("{:20s} {:6d}".format(eintrag[0], eintrag[2]))
