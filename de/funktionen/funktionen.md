
# Funktionen selbst schreiben

### Aufgabe 3

Schreibe eine Funktion, die eine Summe berechnet. Vervollständige das Programm, indem Du in die Lücken einsetzt: `anzahlen`, `daten`, `def`, `return`, `summe_berechnen', `+=`

    ____ summe_berechnen(daten):
        gesamt = 0
        for anzahl in ____:
            gesamt ____ anzahl
        ____ gesamt

    anzahlen = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]
    summe = ____(____)
    print(summe)


### Aufgabe 4

Schreibe eine Funktion, die aus einer Liste von Zahlen und einer gegebenen Grundgesamtheit einen prozentualen Anteil berechnet. Verwende den folgenden Aufbau:

    def anteil_berechnen(daten, grundgesamtheit):

        # hier eigenen Code einsetzen

        return anteil


    testdaten = [1, 2, 3, 4]
    prozent = anteil_berechnen(testdaten, 100.0)
    if prozent == 10:
        print("Test erfolgreich!")


### Aufgabe 5

Erstelle eine neue Datei `bigbang_anzahl.txt` mit folgendem Inhalt:

    12562
    2178
    342
    129
    384
    208
    164
    82
    41

Berechne die durchschnittliche Anzahl aus der Datei. Schreibe Dir dazu (mindestens) zwei Funktionen:

    def datei_lesen(dateiname):
        ...

    def durchschnitt(daten):
        ...

Finde selbst heraus, was die Funktionen mit `return` zurückliefen sollen.

**TIP:** Du kannst auch zuerst das Programm ohne Funktionen schreiben und danach die Funktionen aus dem Code ausgliedern.


### Aufgabe 6

Folgendes Programm berechnet die Standardabweichung aus der Datei `bigbang_anzahl.txt`. Wir möchten die Berechnung verallgemeinern. Packe den Code zur Berechnung der Standardabweichung in eine Funktion.

    import math

    daten = []
    for line in open('bigbang_anzahl.txt'):
        daten.append(int(line.strip()))

    avg = durchschnitt(daten)

    stdsum = 0.0
    for zahl in daten:
        stdsum += (zahl - avg) ** 2
    varianz = stdsum / len(daten)
    stabw = math.sqrt(varianz)

    print("Standardabweichung: {:8.2f}".format(stabw))

### Aufgabe 7

Erkläre das Programm `parameter.py`:

    def addition(a=2, b=2, c=2):
        return a + b + c


    print(addition(3, 3, 3))
    print(addition(3, 3))
    print(addition(3))
    print(addition())
    print(addition(b=4))
    print(addition(b=4, c=5))


### Aufgabe 8

Erkläre das Programm `fakultaet.py`:

    def fakultaet(zahl):
        """Berechnet die Fakultaet der gegebenen Zahl."""
        if zahl > 1:
            return zahl * fakultaet(zahl - 1)
        else:
            return 1

    x = int(input('Bitte gib eine Zahl ein: '))
    y = fakultaet(x)
    print ("Das Ergebnis ist:\n{}! = {}}".format(x, y))
