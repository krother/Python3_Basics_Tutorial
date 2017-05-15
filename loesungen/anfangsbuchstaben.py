"""
Häufigste Anfangsbuchstaben berechnen

Beispiel für Dictionaries
"""


# erzeuge ein leeres Dictionary
d = {}

# Lies eine Datei mit Babynamen ein
for zeile in open("names/yob2014.txt"):
    spalten = zeile.strip().split(',')
    name = spalten[0]
    if spalten[1] == 'M':
        # Ermittle den Anfangsbuchstaben
        erster = name[0]
        # Wenn es für den Anfangsbuchstaben im Dictionary
        # noch keinen Eintrag gibt, setze diesen auf 0
        d.setdefault(erster, 0)
        # Zähle den Eintrag um 1 hoch
        d[erster] += 1


# Gib alle Einträge im Dictionary alphabetisch sortiert aus
for k in sorted(d):
    print("{:s}{:8d}".format(k, d[k]))


# Um nach der Anzahl zu sortieren,
# müssen wir das dictionary in eine Liste umwandeln
tabelle = []
for k in d:
    tabelle.append([d[k], k])
tabelle.sort(reverse=True)
print(tabelle[:3])  # Top 3 ausgeben
