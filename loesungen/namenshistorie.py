"""
Namensentwicklung über die letzten 135 Jahre ermitteln
und als Diagramm darstellen.
"""
import pylab as plt

suchname = "Harley"
suchgeschlecht = "F"

jahre = []
anzahlen = []

for jahr in range(1880, 2015):
    print(jahr)
    dateiname = "names/yob{}.txt".format(jahr)
    anz_gefunden = 0  # möglich, daß Name in einem Jahr nicht vorkommt
    for zeile in open(dateiname):
        spalten = zeile.strip().split(',')
        name = spalten[0]
        geschlecht = spalten[1]
        if name == suchname and geschlecht == suchgeschlecht:
            anz_gefunden = int(spalten[2])
    # beide append's stehen zusammen,
    # damit die Listen ganz sicher gleich lang sind
    jahre.append(jahr)
    anzahlen.append(anz_gefunden)

# Rohdaten ausgeben
print(len(jahre), jahre)
print(len(anzahlen), anzahlen)

# plotten
plt.figure()
plt.plot(jahre, anzahlen, 'b-')
plt.title('Häufigkeit von "{}" in den USA'.format(suchname))
plt.xlabel('Jahr')
plt.ylabel('Namenshäufigkeit')
plt.savefig('{}.png'.format(suchname), dpi=150)
