
# Inhalte parsen

Textdateien enthalten meist sowohl Text als auch Zahlen. Diese aus dem Text zu ermitteln und *strukturiert* in Variablen abzulegen nennt man **parsen**. Dazu benötigen wir Funktionen von Strings, Listen und **Typumwandlungen**.


### Aufgabe 1

Setze die folgenden Teile in den Code ein, so daß alle Befehle korrekt ausgeführt werden: `alter`, `int(alter)`, `name`, `str(geboren)`, `2000`

    name = 'Emily Smith'
    geboren = _____
    ____ = '15'

    text = ____ + ' kam im Jahr ' + _____ + ' zur Welt.'
    jahr = geboren + _____
    text
    jahr


### Aufgabe 2

Das folgende Programm sammelt Namen, die mindestens 10000x verwendet wurden in einer Liste. Leider enthält das Programm **vier Fehler**. Finde und korrigiere diese.


    häufige = []

    for line in open('names/yob2015.txt'):
        spalten = line.strip().split(',')
        name = spalten[1]
        anzahl = int(spalten[3])
        if anzahl >= 10000
            häufige.append(name)

    print(haeufige)


### Aufgabe 3

Schreibe ein Programm, welches die Gesamtzahl der Babys für das Jahr 2015 berechnet und ausgibt. Vergleiche das Ergebnis mit dem für das Jahr 1915.


### Aufgabe 4

Schreibe ein Programm, welches *die drei häufigsten* Vornamen für Jungen und Mädchen in jedem Jahrgang ermittelt und ausgibt.

**Hinweis:** Die häufigsten drei Namen sind zugleich die ersten in der Liste.


### Aufgabe 5

Schreibe ein Programm, welches den prozentualen Anteil der 10 häufigsten Namen für das Jahr 2015 berechnet und ausgibt.

