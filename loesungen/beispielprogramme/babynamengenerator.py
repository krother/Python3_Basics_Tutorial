"""
Aufgabe: Erweiterter Babynamengenerator

- Das Programm gibt zufällig Namen aus der Babynamendatei aus.
- Nur Jungen- oder Mädchennamen werden ausgeben
"""
import random

geschlecht = 'F'
dateiname = 'names/yob2014.txt'

namen = []

for line in open(dateiname):
    spalten = line.strip().split(',')
    if spalten[1] == geschlecht:
        namen.append(spalten[0])

# Das Programm macht 10 Vorschläge
for i in range(10):
    zufallsname = random.choice(namen)
    print(zufallsname)
