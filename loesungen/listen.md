
# Listen

## Lösungen - Listen verarbeiten

### Aufgabe 3

Wir können die Zahlen aus einer Liste mit Hilfe einer Hilfsvariable aufsummieren.
Über die Liste läßt sich mit einer `for`-Schleife iterieren:

    top8 = [34465, 32025, 28569, 27531, \
            24928, 23632, 22818, 22307]

    gesamt = 0
    for anzahl in top8:
        gesamt = gesamt + anzahl
       
    print(gesamt)


### Aufgabe 4

Die zwei Bedingungen *"Anfangsbuchstabe A"* und *"Anfangsbuchstabe M"* lassen sich mit zwei `if`-Anweisungen umsetzen:

    namenliste = ['Emily', 'Hannah', 'Madison', 'Ashley', 'Sarah', 
             'Alexis', 'Samantha', 'Jessica', 'Elizabeth', 'Taylor', 
             'Lauren', 'Alyssa', 'Kayla', 'Abigail', 'Brianna', 
             'Olivia', 'Emma', 'Megan', 'Grace', 'Victoria']

    for name in namenliste:
        if name[0] == 'A':
            print(name)
        if name[0] == 'M':
            print(name)

Ein `if..elif` funktioniert ebenfalls:

    for name in namenliste:
        if name[0] == 'A':
            print(name)
        elif name[0] == 'M':
            print(name)

Auch die Verknüpfung zweier Bedingungen mit `or` führt zum gleichen Ergebnis:

    for name in namenliste:
        if name[0] == 'A' or name[0] == 'M':
            print(name)

#### Achtung:

Folgender Ausdruck **führt zu einem falschen Ergebnis**:

    for name in namenliste:
        if name[0] == 'A' or 'M':
            print(name)

Der Grund ist, dass Python `'M'` als eigenen Boole'schen Ausdruck wertet. Der Wahrheitswert von einem nicht-leeren String ist immer `True`. Deshalb trifft die Bedingung immer zu.

