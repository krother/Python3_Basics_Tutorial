
# Anweisungen wiederholen

In unseren ersten Programmen wurde jeder Python-Befehl genau ein Mal ausgeführt. Strenggenommen macht das die ganze Programmiererei ein wenig sinnlos, weil unsere Programme durch unsere Tippgeschwindigkeit ausgebremst werden.

In diesem Abschnitt werden wir uns daher die `for`-Anweisung genauer anschauen, mit der wir einen oder mehrere Befehle wiederholt ausführen können.


### Aufgabe 1

Was tut das folgende Programm?

    for zahl in range(1, 43):
        print(zahl)


### Aufgabe 2

Erkläre, warum die `for`-Anweisung besser als der folgende Ansatz ist:

    print(1)
    print(2)
    print(3)
    print(4)
    ..
    print(42)


### Aufgabe 3

Schreibe eine Schleife mit `for`, welche folgende Ausgabe produziert:

    1
    4
    9
    16
    25
    36
    49


### Aufgabe 4

Erkläre den Unterschied zwischen den folgenden zwei Programmen:

    summe = 0
    for number in range(10):
        summe = summe + number
        print(summe)

und

    summe = 0
    for number in range(10):
        summe = summe + number
    print(summe)


### Aufgabe 5

Was tut das folgende Programm?

    text = ""
    characters = "Hannah"
    for char in characters:
        text = char + text
    print(text)


### Aufgabe 6

Schreibe ein Programm, welches die Anzahl der Buchstaben im Namen `Stefani Joanne Angelina Germanotta` ermittelt. **Leerzeichen zählen mit!**

