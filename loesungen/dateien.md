
# Dateien lesen und schreiben

## Lösungen - Textdateien einlesen

### Aufgabe 3

Das sortierte Programm lautet:

    girls = 0

    for line in open('names/yob2015.txt'):
        if "B" in line:
            if ",F," in line:
                girls += 1

    print(girls)


### Aufgabe 6

Die einfachste Variante zum Finden eines Namens verwendet den `in`-Operator:

    for zeile in open('names/yob2015.txt'):
        if "Sheldon" in zeile:
            print(zeile)

----

## Lösungen - Textdateien parsen

### Aufgabe 2

Die vier Fehler sind:

* Fehlender Doppelpunkt am Ende der Zeile mit `if`
* In der Variable `haeufige` wird der Umlaut inkonsistent verwendet.
* Die Indices `[1]` und `[3]` müssen jeweils um eins kleiner sein.

