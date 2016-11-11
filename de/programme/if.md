
# Entscheidungen treffen

Mit den bisherigen Python-Befehlen lassen sich bereits eine ganze Menge unterschiedliche Programme schreiben. Es fehlt uns allerdings noch eine wichtige Möglichkeit: Im Programm *Entscheidungen zu treffen*. In Python gibt es dafür die `if`-Anweisung.

Mit diesem Befehl sind wir theoretisch in der Lage, jedes erdenkliche Programm zu schreiben (die Leute am Institut für Informatik nennen das *"Turing-vollständig"*). Trotzdem geht der Kurs noch weiter, denn *"Turing-vollständig"* bedeutet nicht automatisch *"schnell und bequem"*.

Wir schauen uns trotzdem erst einmal an, wie der `if`-Befehl funktioniert. Für die folgenden Übungen benötigen wir den offiziellen Datensatz von Babynamen. Du kannst die Dateien von der Seite [http://www.ssa.gov/oact/babynames/limits.html](http://www.ssa.gov/oact/babynames/limits.html) herunterladen (es genügt die nicht nach Bundesstaaten aufgeschlüsselte Variante). 


### Aufgabe 1

Führe das folgende Programm aus. Was wird berechnet?

    boys = 0
    girls = 0
    for line in open('yob2014.txt'):
        if ",M," in line:
            boys = boys + 1
        elif ",F," in line:
            girls = girls + 1
        else:
            print("Zeile nicht erkannt:\n", line)
    print(boys, girls)


### Aufgabe 2

Welche der folgenden `if`-Anweisungen ist syntaktisch korrekt?

* `if a and b:`
* `if len(s) == 23:`
* `if a but not b < 3:`
* `if a ** 2 >= 49:`
* `if a != 3`
* `if (a and b) or (c and d):`


### Aufgabe 3

Schreibe ein Programm, in dem Du einen Namen über die Tastatur eingeben kannst. Finde die Zeile(n) mit diesem Namen in der Datei `yob2014.txt` und gib diese auf dem Bildschirm aus.


### Aufgabe 4

Gegeben ist eine Liste der 20 beliebtesten Mädchennamen aus dem Jahr 2000:

    ['Emily', 'Hannah', 'Madison', 'Ashley', 'Sarah', 
    'Alexis', 'Samantha', 'Jessica', 'Elizabeth', 'Taylor', 
    'Lauren', 'Alyssa', 'Kayla', 'Abigail', 'Brianna', 
    'Olivia', 'Emma', 'Megan', 'Grace', 'Victoria']

Schreibe ein Programm, das alle Namen ausgibt, die mit einem `'A'` anfangen.


### Aufgabe 5

Wie viele Babynamen aus dem Jahr 1900 fingen mit einem `'M'` an?

Wie viele waren es 2014?


### Aufgabe 6

Wie viele unterschiedliche *Mädchennamen* mit `'M'` gab es 2014?

