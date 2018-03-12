
# Entscheidungen treffen

**Wie oft kommte der Buchstabe 'C' vor?**

![Buchstabensalat](list.png)

Mit den bisherigen Python-Befehlen lassen sich bereits eine ganze Menge unterschiedliche Programme schreiben. Es fehlt uns allerdings noch eine wichtige Möglichkeit: Im Programm *Entscheidungen zu treffen*. In Python gibt es für Entscheidungen (Verzweigungen) die `if`-Anweisung. Darum geht es in diesem Kursteil.

### Aufgabe 1

Führe das folgende Programm aus und erkläre die Ausgabe:

    zahl = input("Bitte gib eine Zahl ein")

    if zahl > 10:
        print("Die Zahl ist größer als 10.")
    elif zahl == 10:
        print("Die Zahl ist genau 10.")
    else:
        print("Die Zahl ist kleiner als 10.")


### Aufgabe 2

Das folgende Programm soll die Positionen aller Buchstaben *"n"* im Namen ausgeben. Leider enthält das Programm **drei Fehler**. Bringe das Programm zum Laufen:

    name = "Anna"
    position = 1

    for buchstabe in name
        if buchstabe = "n":
            print(position)
    position = position + 1


### Aufgabe 3

Gegeben ist eine Liste der 20 beliebtesten Mädchennamen aus dem Jahr 2000:

    ['Emily', 'Hannah', 'Madison', 'Ashley', 'Sarah', 
    'Alexis', 'Samantha', 'Jessica', 'Elizabeth', 'Taylor', 
    'Lauren', 'Alyssa', 'Kayla', 'Abigail', 'Brianna', 
    'Olivia', 'Emma', 'Megan', 'Grace', 'Victoria']

Schreibe ein Programm, das alle Namen ausgibt, die mit einem `'A'` oder `'M'` anfangen.


### Aufgabe 4

<quiz name="">
    <question multiple>
<p>Welche der folgenden <code>if</code>-Anweisungen sind syntaktisch korrekt?</p>
    <answer correct><code>if a and b:</code></answer>
    <answer correct><code>if len(s) == 23:</code></answer>
    <answer><code>if a but not b &lt; 3:</code></answer>
    <answer correct><code>if a ** 2 >= 49:</code></answer>
    <answer><code>if a != 3</code></answer>
    <answer correct><code>if (a and b) or (c and d):</code></answer>
    <explanation>Es sind ein Wahrheitsausdruck und eine Doppelpunkt am Ende notwendig.</explanation>
    </question>
</quiz>
