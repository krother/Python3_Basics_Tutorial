
# Anweisungen wiederholen

In unseren ersten Programmen wurde jeder Python-Befehl genau ein Mal ausgeführt. Streng genommen macht das die ganze Programmiererei ein wenig sinnlos, weil unsere Programme durch unsere Tippgeschwindigkeit ausgebremst werden.

In diesem Abschnitt werden wir uns daher die `for`-Anweisung genauer anschauen, mit der wir einen oder mehrere Befehle wiederholt als **Schleife** ausführen können.

![Schleife](schleife_python.png)

### Aufgabe 1

Was tut das folgende Programm?

    filme = ["Star Wars", "Star Trek", "Ratatouille"]
    for f in filme:
        print(f)

### Aufgabe 2

Was tut das folgende Programm?

    for zahl in range(1, 43):
        print(zahl)


### Aufgabe 3

Erkläre, warum die `for`-Anweisung besser als der folgende Ansatz ist:

    print(1)
    print(2)
    print(3)
    print(4)
    ..
    print(42)


### Aufgabe 4

Schreibe eine Schleife mit `for`, welche folgende Ausgabe produziert:

    1
    4
    9
    16
    25
    36
    49


### Aufgabe 5

Zeichne vier Quadrate:

![](four_squares.svg)

### Aufgabe 6

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


### Aufgabe 7

Zeichne konzentrische Quadrate. Du kannst mit `turtle.up()` und `turtle.down()` das Zeichnen aus- und anschalten.

![](concentric.svg)



### Aufgabe 8

<quiz name="">
    <question multiple>
        <p>Welche der folgenden Befehle sind korrekt?</p>
        <answer correct><code>for char in "ABCD":</code></answer>
        <answer correct><code>for i in range(10):</code></answer>
        <answer><code>for k in 7.65:</code></answer>
        <answer correct><code>for number in [4, 6, 8]:</code></answer>
        <answer><code>for (i=0; i&lt;10; i++):</code></answer>
        <explanation>for-Schleifen lassen sich auf aufzählbare Typen wie Strings, Listen, Generatoren (range) und Dateien anwenden. Floats und Integers funktionieren jedoch nicht.</explanation>
    </question>
</quiz>


### Aufgabe 9

Zeichne eine Spirale. 

![](square_spiral.svg)
