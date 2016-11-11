
# Mehrere Dateien verarbeiten

### Aufgabe 1

Das folgende Programm berechnet die Gesamtzahl der Geburten der vergangenen 130 Jahre.

Im Programm versteckt sich ein *subtiler semantischer Fehler*. Führe das Programm aus. Inspiziere die Ausgabe. Finde und repariere den Fehler.


    geburten = []
    summe = 0

    print("\nJahr    Geburten pro Jahr")
    print("-" * 25)
    for jahr in range(1890, 2015, 1):
        filename = 'names/yob{}.txt'.format(jahr)
        for zeile in open(filename):
            spalten = zeile.strip().split(',')
            geburten.append(int(spalten[2]))
        print("{:4d}    {:>8d}".format(jahr, sum(geburten)))
        summe += sum(geburten)
    print("\nErgebnis: {} Geburten insgesamt".format(summe))


### Aufgabe 2

Schreibe ein Programm, welches

* Den Benutzer nach einem Namen fragt.
* Die Datei `yob2000.txt` einliest.
* Alle Zeilen, die diesen Namen enthalten, ausgibt.

### Aufgabe 3

Erweitere das Programm, so daß es auch nach dem Geschlecht fragt. Gib nur die Zeilen mit Übereinstimmung in der Spalte mit `'M'` oder `'F'` aus.

### Aufgabe 4

Ersetze die `input`-Befehle durch eine Variable, damit das wiederholte Eintippen von Name usw. nicht so nervig ist.

### Aufgabe 5

Erweitere das Programm, so daß es *alle* Dateien von 1880 bis 2014 einliest und die Übereinstimmungen ausgibt.

### Aufgabe 6

Sammle alle Übereinstimmungen aus dem vorigen Programm in einer einzigen Tabelle. Füge eine Spalte für das Jahr hinzu. Speichere die Tabelle in einer Textdatei.

### Aufgabe 7

Fall in einem Jahrgang keine Übereinstimmung gefunden wurde, füge eine `0` dem Ergebnis hinzu.


### Aufgabe 8

Erweitere das Programm so, daß es mehrere Namen auf einmal untersuchen kann. Die zu suchenden Namen sollen in einer Liste am Anfang des Programms stehen.

### Aufgabe 9

Untersuche die Beliebtheit der Vornamen folgender US-Promis im Verlauf der letzten 130 Jahre:

| Name            | Kommentar                      |
|-----------------|--------------------------------|
| Lance Armstrong | erster Mensch auf dem Mond |
| Madonna | Hitsingle "Like a Prayer" |
| Osama Bin Laden | wird zum Drahtzieher der 9/11 Anschläge erklärt |
| Barack Obama    | erster afroamerikanischer Präsident der USA |
| Katrina         | gleichnamiger Hurrikan verwüstet New Orleans |
| Leonidas        | Der Film '300' erscheint in den Kinos |
| Angelina Jolie  | Skandal um Affäre mit Brad Pitt |
| Achilles        | 'Troja' mit Brad Pitt erscheint in den Kinos |
| Prinzessin Leia | Der Film 'Star Wars' erscheint in den Kinos |
| Frida Kahlo     | Ihr Leben erscheint als Broadway-Musical |
| Arielle         | Ihr Leben wird von Walt Disney verfilmt |
| Arnold Schwarzenegger | 'Terminator 2' erscheint in den Kinos |
| Daenerys Targaryen | Die Buch/Filmserie 'Game of Thrones' erscheint |
| Khaleesi | offizieller Titel von Daenerys Targaryen |
| Tyrion Lannister | Die Buch/Filmserie 'Game of Thrones' erscheint |
