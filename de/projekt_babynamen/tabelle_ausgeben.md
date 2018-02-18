
# Dateien schreiben

### Aufgabe 1

Bilde Paare aus Python-Anweisungen und deren Bedeutungen.

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

Ergänze die folgenden Anweisungen durch `int()` oder `str()`, so daß sie alle funktionieren.

     In [1]: 9 + 9

     In [2]: 9 + '9'

     In [3]: '9' + '9'

     In [4]: 9 * '9'


### Aufgabe 5

Schreibe ein Programm, welches die folgenden Daten in eine zweispaltige Textdatei schreibt.

    namen = ["Emma", "Olivia", "Sophia", "Isabella", 
             "Ava", "Mia", "Emily"]
    anzahlen = [20799, 19674, 18490, 16950, 
               15586, 13442, 12562]


# Tabellen

Daten treten häufig in Form von Tabellen auf. Um Tabellen in Python zu verarbeiten, kommt uns entgegen, daß wir Listen in anderen Listen speichern können. Diese nennt man auch **verschachtelte Listen**. 

Damit sieht eine einfache Tabelle in Python so aus:

    # Spalten: Name, #California, #New York
    [
      ["Emily", 2269, 881],
      ["Amy", 542, 179],
      ["Penny", 54, 12],
      ["Bernadette", 21, 11]
    ]

In diesem Teil des Kurses werden wir uns mit Aufbau und Verarbeitung von verschachtelten Listen beschäftigen.


### Aufgabe 1

Gib alle Zeilen der obigen Tabelle mit einer `for`-Schleife aus.


### Aufgabe 2

Gib alle *Zellen* der obigen Tabelle mit einer *doppelten* `for`-Schleife aus.


### Aufgabe 3

Erzeuge eine Tabelle mit 10x10 Zellen und fülle sie mit den Zahlen von 1 bis 100.


### Aufgabe 4

Sortiere die obige Tabelle nach der zweiten Spalte. Der folgende Codeschnipsel könnte dabei nützlich sein:

    from operator import itemgetter
    tabelle.sort(key=itemgetter(spaltennr))




# Strings formatieren

### Aufgabe 1

Probiere folgende Ausdrücke in der IPython Shell aus:

    "{}".format("Hallo")
    "{:10}".format("Hallo")
    "{:>10}".format("Hallo")
    "{1} {0}".format("Erster", "Zweiter")
    "{:5d}".format(42)
    "{:4.1f}".format(3.14159)
    "{:6.3f}".format(3.14159)
        

### Aufgabe 2

Schreibe eine `for`-Schleife, die den folgenden String produziert:

    000111222333444555666777888999


### Aufgabe 3


Gegeben sind die folgenden zwei Listen:

    top_ten_namen = ['Jacob', 'Michael', 'Matthew', 'Joshua', \
        'Christopher', 'Nicholas', 'Andrew', 'Joseph', \
        'Daniel', 'Tyler']

    top_ten_zahlen = [34465, 32025, 28569, 27531, \
        24928, 23632, 22818, 22307, 21500]

Schreibe ein Programm, welches alle Namen und Zahlen als Tabelle
mit ausgerichteten Spalten ausgibt.



### Aufgabe 3

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

### Aufgabe 4

Erweitere das Programm aus der vorigen Aufgabe so, dass die Anzahl der Jungen- und Mädchennamen getrennt gezählt und ausgegeben werden.


