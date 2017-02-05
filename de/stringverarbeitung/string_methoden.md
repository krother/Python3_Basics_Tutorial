
# Methoden von Strings

### Aufgabe 1

Finde heraus, was die Ausdrücke mit dem String in der Mitte tun.

![string exercise](../exercises/strings.png)

### Aufgabe 2

Das folgende Programm findet Namen, die sowohl für Jungen und Mädchen gebräuchlich sind und schreibt diese in eine Datei.

Vervollständige den Code zum Unterteilen der Zeilen in Tabellenspalten an der angegebenen Stelle, so daß die Variablen `name` und `geschlecht` definiert sind.


    maedchen = []
    duplikate = []

    for zeile in open('names/yob2015.txt'):
        
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

