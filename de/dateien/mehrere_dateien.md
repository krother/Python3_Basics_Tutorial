
# Mehrere Dateien verarbeiten

### Aufgabe 1

Das folgende Programm berechnet die Gesamtzahl der Geburten der vergangenen 130 Jahre.

Im Programm versteckt sich ein *subtiler semantischer Fehler*. Führe das Programm aus. Inspiziere die Ausgabe. Finde und repariere den Fehler.


    geburten = []
    summe = 0

    print("\nJahr    Geburten pro Jahr")
    print("-" * 25)
    for jahr in range(1890, 2015, 1):
        filename = 'names/yob{}.txt'.format(jahr)
        for zeile in open(filename):
            spalten = zeile.strip().split(',')
            geburten.append(int(spalten[2]))
        print(jahr, sum(geburten))
        summe += sum(geburten)
    print("\nErgebnis: {} Geburten insgesamt".format(summe))


### Aufgabe 2

Schreibe ein Programm, welches Zeilen mit Deinem Namen in den Jahrgängen von 1880 bis 2014 ausgibt.

### Aufgabe 3

Erweitere das Programm, so daß auch das Geschlecht vorgegeben ist. Gib nur die Zeilen mit Übereinstimmung in der Spalte mit `'M'` oder `'F'` aus.

### Aufgabe 4

Sammle sämtliche Übereinstimmungen in einer Liste


### Aufgabe 5

Falls in einem Jahrgang keine Übereinstimmung gefunden wurde, füge eine `0` dem Ergebnis hinzu.
