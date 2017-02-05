
# Entscheidungen treffen

Mit den bisherigen Python-Befehlen lassen sich bereits eine ganze Menge unterschiedliche Programme schreiben. Es fehlt uns allerdings noch eine wichtige Möglichkeit: Im Programm *Entscheidungen zu treffen*. In Python gibt es für Entscheidungen (Verzweigungen) die `if`-Anweisung. Darum geht es in diesem Kursteil.

### Aufgabe 1

Führe das folgende Programm und erkläre die Ausgabe:

    name = "Anna"
    anzahl = 4322

    if "A" in name:
        print("es kommt ein A im Namen vor.")
    if anzahl > 1000:
        print("Die Anzahl ist größer als 1000.")
        if name != "Elizabeth":
            print(".. und der Name nicht Elisabeth")
    elif anzahl == 1000:
        print("Die Anzahl ist genau 1000.")
    else:
        print("Die Anzahl ist kleiner als 1000.")
    if name[0] == "A" and anzahl > 100:
        print("ein Name mit A, der öfter als 100 Mal vorkommt.")


### Aufgabe 2

Gegeben ist eine Liste der 20 beliebtesten Mädchennamen aus dem Jahr 2000:

    ['Emily', 'Hannah', 'Madison', 'Ashley', 'Sarah', 
    'Alexis', 'Samantha', 'Jessica', 'Elizabeth', 'Taylor', 
    'Lauren', 'Alyssa', 'Kayla', 'Abigail', 'Brianna', 
    'Olivia', 'Emma', 'Megan', 'Grace', 'Victoria']

Schreibe ein Programm, das alle Namen ausgibt, die mit einem `'A'` oder `'M'` anfangen.



### Aufgabe 3

Sammle **Operatoren**, **Datentypen**, **Funktionen** und **Python-Befehle**, die Du bisher kennen gelernt hast als Tabelle.

