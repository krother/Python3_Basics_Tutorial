
# Dateien schreiben

### Aufgabe 1

Bilde Paare aus Python-Anweisungen und deren Bedeutugen.

![file exercise](../exercises/files.png)


### Aufgabe 2

Führe das folende Programm aus. Erkläre was passiert.

    namen = ['Adam', 'Bob', 'Charlie']

    f = open('jungs.txt', 'w')
    for name in namen:
        f.write(name + '\n')
    f.close()

### Aufgabe 3

Lösche das `+ '\n'` aus dem Programm und führe es noch einmal aus. Was passiert?


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


### Aufgabe 4

Welche Befehle sind korrekt?

* `for line in open(filename):`
* `f = open(filename, 'w')`
* `open(filename).writelines(out)`
* `f.close()`


### Aufgabe 5

Schreibe ein Programm, welches die folgenden Daten in eine zweispaltige Textdatei schreibt.

    namen = ["Emma", "Olivia", "Sophia", "Isabella", 
             "Ava", "Mia", "Emily"]
    anzahlen = [20799, 19674, 18490, 16950, 
               15586, 13442, 12562]
