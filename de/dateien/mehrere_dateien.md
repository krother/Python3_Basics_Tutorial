
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

Schreibe ein Programm, welches alle Zeilen einer Datei, die einen bestimmten Namen enthalten, ausgibt.
Das Programm beginnt folgendermaßen:

    name = "Harley"
    dateiname = "yob2000.txt"


### Aufgabe 3

Erweitere das Programm, so daß auch das Geschlecht in einer Variablen vorgegeben ist. Gib nur die Zeilen mit Übereinstimmung in der Spalte mit `'M'` oder `'F'` aus.

### Aufgabe 4

Erweitere das Programm, so daß es *alle* Dateien von 1880 bis 2014 einliest und die Übereinstimmungen ausgibt.

### Aufgabe 5

Untersuche die Beliebtheit der Vornamen folgender US-Promis im Verlauf der letzten 130 Jahre:

| Name            | Kommentar                      |
|-----------------|--------------------------------|
| Lance Armstrong | erster Mensch auf dem Mond |
| Madonna         | Hitsingle "Like a Prayer" |
| Barack Obama    | Präsident der USA |
| Katrina         | Hurrikan verwüstet New Orleans |
| Leia            | Der Film 'Star Wars' erscheint in den Kinos |
| Frida Kahlo     | Ihr Leben erscheint als Broadway-Musical |
| Arielle         | Ihr Leben wird von Walt Disney verfilmt |
| Arnold          | 'Terminator 2' erscheint im Kino |
| Daenerys        | Figur aus 'Game of Thrones' |
| Tyrion          | Figur aus 'Game of Thrones' |

Gib alle Übereinstimmungen mit *Jahr* und *Anzahl* auf dem Bildschirm aus.

### Aufgabe 6

Speichere alle Übereinstimmungen in einer Textdatei.

### Aufgabe 7

Falls in einem Jahrgang keine Übereinstimmung gefunden wurde, füge eine `0` dem Ergebnis hinzu.


### Aufgabe 8

Vervollständige die zuvor erstellte Tabelle mit **Operatoren**, **Datentypen**, **Funktionen** und **Python-Befehlen**.
