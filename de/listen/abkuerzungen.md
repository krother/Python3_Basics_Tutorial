
# Hilfsfunktionen

In Python gibt es zahlreiche Funktionen (und noch mehr Erweiterungsmodule), die einem das Leben erleichtern. Bei der Arbeit mit Listen (und verschachtelten Listen) erweisen sich vor allem folgende Funktionen als nützlich:

* `enumerate()`
* `sum()`
* `range()`
* `zip()`

In den nächsten Aufgaben werden wir Codebeispiele mit diesen Funktionen vereinfachen.

### Aufgabe 1

Vereinfache das folgende Programm:

    anzahlen = [356, 412, 127, 8, 32]

    gesamt = 0
    for anz in anzahlen:
        gesamt = gesamt + anz
    print(gesamt)


### Aufgabe 2

Vereinfache das folgende Programm:

    i = 0
    while i < 10:
        print(i * '*')
        i += 1


### Aufgabe 3

Vereinfache das folgende Programm:

    namen = ['Lilly', 'Lily', 'Leila', 'Lilja', 'Lillie']
    anzahlen = [356, 412, 127, 8, 32]

    tabelle = []
    i = 0
    while i < len(namen):
        row = (namen[i], anzahlen[i])
        tabelle.append(row)
        i += 1
    print(tabelle)


### Aufgabe 4

Vereinfache das folgende Programm:

    namen = ['Lilly', 'Lily', 'Leila', 'Lilja', 'Lillie']

    i = 0
    for name in namen:
        print(i, name)
        i += 1


### Aufgabe 5

Verwende `range()`, um die folgenden Listen zu erstellen:

* `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
* `[4, 7, 9, 12]`
* `[10, 20, 30, 40, 50]`
* `[5, 4, 3, 2, 1]`
* `[33, 32, 31, 30]`


### Aufgabe 6

Das folgende Programm soll Namen und dazugehörige Anzahlen paarweise ausgeben.
Leider enthält das Programm **drei Defekte**. Finde und behebe diese.


    namen = ['Jacob', 'Michael', 'Matthew', 'Joshua', 'Christopher', 
                 'Nicholas', 'Andrew' 'Joseph', 'Daniel', 'Tyler']

    anzahlen [34465, 32025, 28569, 27531, 24928,
                 24928, 23632, 22818, 22307, 21500]

    if len(namen) == len(anzahlen):
       print("Achtung: die Listen sind unterschiedlich lang!")
       print(len(namen), len(anzahlen))

    for i in range(len(namen)):
        vorname = namen[i]
        anzahl = anzahlen[i]
        print("{:10s} {:6d}".format(vorname, anzahl))


### Aufgabe 7

Vereinfache das Programm mit Hilfe von `zip()`. Du solltest mindestens zwei und maximal fünf Programmzeilen einsparen.
