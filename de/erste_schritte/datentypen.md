
# Datentypen in Python

Bisher haben wir lediglich mit Zahlen gearbeitet. Nun werden wir auch Text in Variablen speichern. 


## Strings


### Aufgabe 1

Probiere die folgenden Anweisungen aus, um Textvariablen oder **Strings** zu erzeugen:

    In [1]: vorname = 'Emily'
    In [2]: nachname = "Smith"
    In [3]: name = vorname + " " + nachname
    In [4]: name

### Aufgabe 2

Was ergeben die folgenden Anweisungen?

    In [5]: name[0]
    In [6]: name[3]
    In [7]: name[-1]
    In [8]: name[0] + name[6]

### Aufgabe 4

Gib die beiden Initialien aus dem folgenden String aus. Verwende die Schreibweise mit eckigen Klammern:

    name = "Walter White"



### Aufgabe 5

Was ist nach der folgenden Befehlsfolge in `name` enthalten? Erkläre den Code:

    In [8]: name = ""
    In [9]: anna = "Anna"
    In [10]: name = anna[0] + name
    In [11]: name = anna[1] + name
    In [12]: name = anna[2] + name
    In [13]: name = anna[3] + name
    In [14]: name


# Listen erstellen

Um größere Datenmengen zu verarbeiten, können wir nicht für jeden Eintrag einen neuen Variablennamen ausdenken. Irgendwie muß es möglich sein, mehrere Datensätze in einer Variable zu speichern. In Python treten an dieser Stelle **Listen** auf die Bühne.

Listen sind eine einfache Abfolge von Elementen. Allerdings zählt Python anders als Menschen:

![Indizierung](indexing.png)



### Aufgabe 1

Bilde Paare von Datentypen und Werten.

![datatype exercise](../exercises/datatypes.png)


### Aufgabe 2

Erstelle eine Tabelle, in der Du nach *einfachen* und *zusammengesetzten* Datentypen unterscheidest.

### Aufgabe 3

Auf welchen Datentypen funktioniert die Funktion `len()`?

* Listen
* Dictionaries
* Strings
* Floats
* Tupel

