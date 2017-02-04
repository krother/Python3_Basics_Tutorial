
# Anweisungen wiederholen

In unseren ersten Programmen wurde jeder Python-Befehl genau ein Mal ausgeführt. Strenggenommen macht das die ganze Programmiererei ein wenig sinnlos, weil unsere Programme durch unsere Tippgeschwindigkeit ausgebremst werden.

In diesem Abschnitt werden wir uns daher die `for`-Anweisung genauer anschauen, mit der wir eine oder mehrere Befehle wiederholt ausführen können.


### Aufgabe 1

Was tut das folgende Programm?

    for zahl in range(1, 43):
        print(zahl)

### Aufgabe 2

Finde drei Vorteile, die `for` gegenüber folgendem Ansatz bietet:

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

Schreibe eine `for`-Schleife, die den folgenden String produziert:

    1 4 9 16 25 36 49 64 81


### Aufgabe 6

Schreibe eine `for`-Schleife, die den folgenden String produziert:

    000111222333444555666777888999


### Aufgabe 7

Was tut das folgende Programm?

    text = ""
    characters = "Hannah"
    for char in characters:
        text = char + text
    print(text)

### Aufgabe 8

Schreibe ein Programm, welches die Anzahl der Buchstaben im Namen `Stefani Joanne Angelina Germanotta` ermittelt. **Leerzeichen zählen mit!**


### Aufgabe 10

Welche der folgenden Befehle sind korrekt?

* `for char in "ABCD":`
* `for i in range(10):`
* `for number in [4, 6, 8]:`
* `for k in 3+7:`
* `for (i=0; i<10; i++):`
* `for var in open('bigbang.txt'):`
