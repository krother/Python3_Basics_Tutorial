
# Programme

## Lösungen - for-Schleifen

### Aufgabe 3

Es gilt, Quadratzahlen auszugeben:

    for zahl in range(1, 8):
        print(zahl ** 2)


### Aufgabe 4

Die Einrückung bestimmt, welche Befehle *als Teil der Schleife* wiederholt werden. Sie ist ein zentrales Syntaxelement in Python.

### Aufgabe 5

TIP: setze folgende Zeile in die For-Schleife:

    print(char, text)

### Aufgabe 6

Selbst ein Monster von Namen wie der von Lady Gaga läßt sich schnell auszählen. Wir brauchen dazu `anzahl`, eine *Zählervariable*:

    name = 'Stefani Joanne Angelina Germanotta'
    anzahl = 0

    for buchstabe in name:
        anzahl = anzahl + 1

    print(anzahl)

#### Anmerkung

Die Funktion `len` löst das Problem mit einer Zeile, auch wenn es darum in dieser Aufgabe nicht ging:

    print(len(name))

----

## Lösungen - Verzweigungen mit if

### Aufgabe 3

Die drei Fehler sind:

* Ein Doppelpunkt fehlt am Ende der for-Anweisung.
* In der Verzweigung mit `if` muß statt `=` ein `==` verwendet werden.
* Die letzte Zeile muß einmal eingerückt werden (um vier Leerzeichen).

----

## Lösungen - Selbsstest

### Leicht

Grade Zahlen lassen sich mit dem Modulo-Operator (`%`) ermitteln:

    for zahl in range(2, 21):
        if zahl % 2 == 0:
            print(zahl)


### Mittel

Wir verwenden wieder einmal eine Zählvariable:

    name = "CSAIPRALKAINACZEYLVOST"
    c = 0

    for buchstabe in name:
        if buchstabe == "C":
            c = c + 1

    print(c)

#### Anmerkung

Auch hier gibt es eine Abkürzung:

    print(name.count("C"))


### Schwer

Der Trick ist hier, eine Zählvariable mitzuführen, die kontinuierlich hochzählt:

    name = "CSAIPRALKAINACZEYLVOST"
    i = 0
    ergebnis = ""

    for buchstabe in name:
        if i % 2 == 1:
           ergebnis = ergebnis + buchstabe
        i = i + 1

    print(ergebnis)
