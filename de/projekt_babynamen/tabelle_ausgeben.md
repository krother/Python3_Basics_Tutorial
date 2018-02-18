
# Tabellen ausgeben

In diesem Kapitel werden wir unsere Ergebnisse in eine **Datei schreiben**. Nicht nur das, wir möchten sie auch **als Tabelle formatieren**.


## Dateien Schreiben

### Aufgabe 1

Bilde Paare aus Python-Anweisungen und deren Bedeutungen.

![file exercise](../exercises/files.png)


### Aufgabe 2

Führe das folende Programm aus. Erkläre was passiert.

    namen = ['Adam', 'Bob', 'Charlie']

    with open('jungs.txt', 'w') as f:
        for name in namen:
            f.write(name + '\n')

<quiz name="">
    <question multiple>
        <p>Markiere alle korrekten Aussagen</p>
        <answer correct>Es werden drei Zeilen in die Datei geschrieben</answer>
        <answer correct>Die Datei entsteht im aktuellen Arbeitsverzeichnis</answer>
        <answer>Es werden zwei Dateien geschrieben: "jungs.txt" und "w"</answer>
        <answer correct>Am Ende des <code>with</code>-Blocks wird die Datei automatisch geschlossen</answer>
        <answer>An jeden Namen wird der Buchstabe 'n' angehängt</answer>
        <explanation></explanation>
    </question>
</quiz>


### Aufgabe 3

Lösche das `+ '\n'` aus dem Programm und führe es noch einmal aus. Was passiert?


## Tabellen

Daten treten häufig in Form von Tabellen auf. Da eine Liste andere Listen enthalten kann, können wir diese **verschachtelte Listen** als einfaches Tabellenformat nutzen: 

    # Name, Babys Kalifornien, Babys New York
    tab = [
      ["Emily", 2269, 881],
      ["Amy", 542, 179],
      ["Penny", 54, 12],
      ["Bernadette", 21, 11]
    ]

Technisch ist an verschachtelten Listen nichts besonderes. Man muss allerdings die richtigen eckigen Klammern für die Indizierung finden, z.B. für die zweite Spalte der dritten Zeile:

    print(tab[2][1])


### Aufgabe 4

Gib alle Namen aus der obigen Tabelle mit einer `for`-Schleife aus.


## Strings formatieren

Um Tabellen und andere Daten hübsch auszugeben, benötigen wir **String-Formatierung**.

### Aufgabe 5

Probiere folgende Ausdrücke in der Python Shell aus:

    "{}".format("Hallo")
    "{} {}".format("Hallo", "Welt")
    "{:10}".format("Hallo")
    "{:>10}".format("Hallo")
    "{:5d}".format(42)
    "{:4.1f}".format(3.14159)
    "Ergebnis: {:6.3f}".format(3.14159)

<quiz name="">
    <question multiple>
        <p>Markiere alle korrekten Aussagen</p>
        <answer correct>Die geschweiften Klammern dienen als Platzhalter</answer>
        <answer correct>Die Argumente der Funktion <code>format()</code> werden in die Platzhalter eingesetzt</answer>
        <answer>Außer den Platzhaltern darf der String keinen Text enthalten</answer>
        <answer correct><code>{:xd}</code> ist ein Platzhalter für eine ganze Zahl mit x Stellen</answer>
        <answer correct>Strings lassen sich rechts- und linksbündig ausgeben</answer>
        <answer><code>{:4.1f}</code> ist ein Platzhalter für eine Fließkommazahl mit vier Stellen vor und einer nach dem Komma</answer>
        <answer>Die geschweiften Klammern werden mit ausgegeben</answer>
        <explanation></explanation>
    </question>
</quiz>


### Aufgabe 6

Gib die Tabelle aus Aufgabe 3 formatiert aus.


### Aufgabe 7

Schreibe die formatierte Tabelle in eine Datei.


## Hilfsfunktionen zum Arbeiten mit Listen

In Python gibt es zahlreiche Funktionen, die eine die Arbeit mit Listen erleichtern. Neben `len()` und `range()` sind vor allem die Funktionen `enumerate()`, `sum()` und `zip()` sind in der Praxis unentbehrlich.


### Aufgabe 8

Das folgende Programm soll Namen und dazugehörige Anzahlen paarweise ausgeben.
Leider enthält das Programm **drei Defekte**. Finde und behebe diese.

    namen = ["Emma", "Olivia" "Sophia", "Isabella", 
             "Ava", "Mia", "Emily"]

    anzahlen [20799, 19674, 18490, 16950, 
               15586, 13442, 12562]

    if len(namen) == len(anzahlen):
       print("Achtung: die Listen sind unterschiedlich lang!")
       print(len(namen), len(anzahlen))

    for name, anzahl in zip(namen, anzahlen):
        print("{:10s} {:6d}".format(namen, anzahl))


### Aufgabe 9

Vereinfache das folgende Programm:

    anzahlen = [356, 412, 127, 8, 32]

    gesamt = 0
    for anz in anzahlen:
        gesamt += anz
    print(gesamt)

<!--sec data-title="Hinweis" data-id="hint-tab-sum"
data-collapse=true ces-->

Die Funktion `sum(x)` akzeptiert eine Liste mit Zahlen als Argument.

<!--endsec-->


### Aufgabe 10

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


<!--sec data-title="Hinweis" data-id="hint-tab-sum"
data-collapse=true ces-->

Die Funktion `zip(x, y)` führt zwei (oder mehr) Listen elementweise zusammen. Verwende eine `for`-Schleife oder `list()`, um das Ergebnis als Liste zu erhalten.

<!--endsec-->


### Aufgabe 11

Vereinfache das folgende Programm:

    namen = ['Lilly', 'Lily', 'Leila', 'Lilja', 'Lillie']

    i = 0
    for name in namen:
        print(i, name)
        i += 1

<!--sec data-title="Hinweis" data-id="hint-tab-sum"
data-collapse=true ces-->

Die Funktion `enumerate(x)` generiert einen Zähler zu einer Liste. Eine übliche Schreibweise ist `for i, elem in enumerate(x)`

<!--endsec-->


## Weitere Übungsaufgaben


### Aufgabe 12

Erzeuge eine Tabelle mit 10x10 Zellen, die nur aus Nullen besteht.


### Aufgabe 13

Erzeuge eine Tabelle mit 10x10 Zellen und fülle sie mit den Zahlen von 1 bis 100.


### Aufgabe 14

Sortiere die Tabelle nach der zweiten Spalte. Verwende folgenden Codeschnipsel:

    from operator import itemgetter

    tab.sort(key=itemgetter(spaltennr))


#### Anmerkung:

An dieser Stelle werden verschachtelte Listen etwas schwerfällig. Mit den Bibliotheken `numpy` und `pandas` werden diese Sachen leichter.