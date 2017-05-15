"""
Ermittle die Gesamtzahl Babys in einem Jahr
"""
summe = 0
for line in open('names/yob2014.txt'):
    anzahl = line.strip().split(',')[2]
    summe += int(anzahl)

print(summe)
