
# Stringverarbeitung

Mit Strings kann man noch eine ganze Menge mehr anstellen.

### Aufgabe 1

Finde heraus, was die Ausdrücke mit dem String in der Mitte tun.

![string exercise](../exercises/strings.png)

### Aufgabe 2

Schreibe eine `for`-Schleife, die den folgenden String produziert:

    1 4 9 16 25 36 49 64 81


### Aufgabe 3

Schreibe eine `for`-Schleife, die den folgenden String produziert:

    000111222333444555666777888999


### Aufgabe 4

Probiere folgende Ausdrücke in der IPython Shell aus:

    "{}".format("Hallo")
    "{:10}".format("Hallo")
    "{:>10}".format("Hallo")
    "{1} {0}".format("Erster", "Zweiter")
    "{:5d}".format(42)
    "{:4.1f}".format(3.14159)
    "{:6.3f}".format(3.14159)
        

### Aufgabe 5

Das folgende Programm findet Namen, die sowohl für Jungen und Mädchen gebräuchlich sind und schreibt diese in eine Datei.

Vervollständige den Code zum Unterteilen der Zeilen in Tabellenspalten an der angegebenen Stelle, so daß die Variablen `name` und `geschlecht` definiert sind.


    maedchen = []
    duplikate = []

    for zeile in open('names/yob2014.txt'):
        
        # hier Code einfuegen
        
        if geschlecht == 'F':
           maedchen.append(name)
        elif geschlecht == 'M':
           if name in maedchen:
               duplicate.append(name)

    output = open('doppelnamen.txt', 'w')
    for name in duplicate:
        text = "{:>15s}\n".format(name)
        output.write(text)
    output.close()
