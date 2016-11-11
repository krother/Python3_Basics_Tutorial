
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

    name = ""
    anna = "Anna"
    name = anna[0] + name
    name = anna[1] + name
    name = anna[2] + name
    name = anna[3] + name
    name

### Aufgabe 4

Mit Strings kann man noch eine ganze Menge mehr anstellen. Finde heraus, was die Ausdrücke mit dem String in der Mitte tun.

![string exercise](../exercises/strings.png)


### Aufgabe 5

Gegeben ist folgende Tabelle

| Zeile      | Wert     |
|------------|----------|
| Vorname    | Tom   |
| Nachname   | O'Malley |
| Geschlecht | M |
| Jahrgang   | 2000  |

Schreibe die Information aus jeder Zeile in eine einzelne Variable.
Verbinde die Variablen anschließend zu einem String, z.B.:

    O'Malley, Tom, M, 2000

