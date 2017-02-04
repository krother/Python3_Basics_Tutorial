
# Text speichern

### Aufgabe 1

Bisher haben wir lediglich mit Zahlen gearbeitet. Nun wenden wir uns auch dem Speichern von Text zu. Probiere die folgenden Anweisungen aus, um Textvariablen oder **Strings** zu erzeugen:

    In [1]: vorname = 'Emily'
    In [2]: nachname = "Smith"
    In [3]: name = vorname + " " + nachname
    In [4]: name

Was tun die folgenden Anweisungen?

    In [5]: name[0]

    In [6]: name[3]
    
    In [7]: name[-1]


### Aufgabe 2

Ist es möglich, die folgenden Sonderzeichen in einem String zu verwenden?

    . 7 @ ? / & * \ Ä ß " ' á

### Aufgabe 3

Was ist nach der folgenden Befehlsfolge in `name` enthalten? Erkläre den Code:

    In [8]: name = ""
    In [9]: anna = "Anna"
    In [10]: name = anna[0] + name
    In [11]: name = anna[1] + name
    In [12]: name = anna[2] + name
    In [13]: name = anna[3] + name
    In [14]: name
