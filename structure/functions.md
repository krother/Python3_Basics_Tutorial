
# Writing your own Functions

Python 3.5 has 72 builtin functions. To start writing useful programs, knowing about 25 of them is sufficient. Many of these functions are useful shortcuts that make your programs shorter.

# Eigene Funktionen

**🎯 Schreibe eigene Funktionen**

### In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 💼 | Mittelwert und Standardabweichung berechnen |
| ⚙ | Funktionen definieren |
| ⚙ | Funktionsparameter |
| ⚙ | Rückgabewerte von Funktionen mit `return` |
| 🔀 | Rekursion |

----
### Aufgabe 1: Summenfunktion

Schreibe eine Funktion, die eine Summe berechnet. Vervollständige das Programm, indem Du in die Lücken einsetzt: `anzahlen`, `daten`, `def`, `return`, `summe_berechnen', `+=`

    ____ summe_berechnen(daten):
        gesamt = 0
        for anzahl in ____:
            gesamt ____ anzahl
        ____ gesamt

    anzahlen = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]
    summe = ____(____)
    print(summe)

----

### Aufgabe 2: Prozente

Schreibe eine Funktion, die aus einer Liste von Zahlen und einer gegebenen Grundgesamtheit einen prozentualen Anteil berechnet. Verwende den folgenden Aufbau:

    def anteil_berechnen(daten, grundgesamtheit):

        # hier eigenen Code einsetzen

        return anteil


    testdaten = [1, 2, 3, 4]
    prozent = anteil_berechnen(testdaten, 100.0)
    if prozent == 10:
        print("Test erfolgreich!")

----

### Aufgabe 3: Mittelwert

Schreibe eine Funktion, die den Mittelwert aus folgenden Zahlen ermittelt:

    :::python3
    def durchschnitt(daten):
        ...

    daten = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]

Finde selbst heraus, was die Funktionen mit `return` zurückliefen sollte.

----

### Aufgabe 4: Standardabweichung

Folgendes Programm berechnet die Standardabweichung aus einer Liste von Zahlen.
Do möchtest die Berechnung verallgemeinern. Packe den Code zur Berechnung der Standardabweichung in eine Funktion.

    import math

    daten = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]

    avg = durchschnitt(daten)

    stdsum = 0.0
    for zahl in daten:
        stdsum += (zahl - avg) ** 2
    varianz = stdsum / len(daten)
    stabw = math.sqrt(varianz)

    print(f"Standardabweichung: {stabw:8.2f}")

----

### Aufgabe 5: Optionale Parameter

Erkläre das Programm `parameter.py`:

    def addition(a=2, b=2, c=2):
        return a + b + c


    print(addition(3, 3, 3))
    print(addition(3, 3))
    print(addition(3))
    print(addition())
    print(addition(b=4))
    print(addition(b=4, c=5))

----

### Aufgabe 6: Rekursion

Erkläre das Programm `fakultaet.py`:

    def fakultaet(zahl):
        """Berechnet die Fakultaet der gegebenen Zahl."""
        if zahl > 1:
            return zahl * fakultaet(zahl - 1)
        else:
            return 1

    x = int(input('Bitte gib eine Zahl ein: '))
    y = fakultaet(x)
    print (f"Das Ergebnis ist:\n{x}! = {y}}")
