
# Selbsttest

### Leicht

Verwende die angegebenen Ausdrücke, um die Liste wie angegeben zu verändern. Verwende jeden Ausdruck genau einmal.

![list funcs exercise2](../exercises/list_funcs2.png)

### Mittel

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


### Schwer

Vereinfache das Programm mit Hilfe von `zip()`. Du solltest mindestens zwei und maximal fünf Programmzeilen einsparen.
