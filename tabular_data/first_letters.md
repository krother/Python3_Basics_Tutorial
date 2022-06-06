
# Anfangsbuchstaben zählen

## In diesem Kapitel lernst Du:

| Bereich | Thema |
|---------|-------|
| 🔀 | Gruppieren von Daten |
| ⚙ | Funktionen definieren |
| 💡 | Methoden von Dictionaries |
| 💡 | Die Funktion `help()` |
| 🔧 | Docstrings schreiben |
| 🐞 | Funktionen einzeln testen |

----

In diesem Kapitel werden wir ein Programm schreiben, das **die häufigsten Anfangsbuchstaben** in Babynamen ermittelt. Dazu benötigen wir den Datentyp **Dictionary**.

----

### Aufgabe 1

Dieses Flussdiagramm zeigt schematisch ein Programm zum Zählen von Anfangsbuchstaben:

![Flussdiagramm](../images/zaehlen.png)

Nimm an, das folgende Datei verarbeitet wird:

    :::bash
    Penny,F,342
    Leonard,M,384
    Sheldon,M,164
    Stuart,M,82

Beantworte folgende Fragen:

1. Was sollte nach Ausführen des Programms im Dictionary stehen?
2. Was wird ausgegeben, wenn die Datei stattdessen leer ist?
3. Durch einen Datenfehler enthält die Eingabedatei eine Leerzeile. An welcher Stelle des Flussdiagramms könnten dadurch Probleme entstehen?

----

### Aufgabe 2

Jetzt fangen wir an, das Programm zu *implementieren*.

Schreibe zuerst den Code für die **erste** und die **letzte** Box im Flussdiagramm.

Im leeren Dictionary kannst Du den Wert für alle Buchstaben auf `0` setzen:

    :::python3
    data = {
    	'A': 0,
    	'B': 0,
    	...
    }

Dies ist nicht die kürzeste Variante, aber am einfachsten zu verstehen.

Stelle sicher, dass das Programm läuft.

----

### Aufgabe 3

Baue als nächstes die Verarbeitung der Datei in das Programm ein. Schreibe dazu den Code für die restlichen Boxen im Flussdiagramm links, sowie die oberste Box rechts (*"nächste Zeile holen"*).

Dazu kannst Du eine `for`-Schleife aus einem früheren Programm *"ausleihen"*.

Stelle sicher, dass das Programm läuft.

----

### Aufgabe 4

Kümmere Dich nun um die Box *"Anfangsbuchstabe ermitteln"*.

Gib den in jeder Zeile ermittelten Anfangsbuchstaben aus.

Stelle sicher, dass das Programm läuft.

----

### Aufgabe 5

Kümmere Dich nun um die restlichen Boxen.

Um einen Wert in einem Dictionary zu erhöhen, kannst Du folgendes Muster verwenden:

    :::python3
    data[schluessel] = data[schluessel] + 1

oder kürzer:

    :::python3
    data[schluessel] += 1

Stelle sicher, dass das Programm läuft.

----

### Aufgabe 6

Vereinfache das Programm (das Erstellen des leeren Dictionaries), indem Du die Methode `d.setdefault()` verwendest.

----

### Aufgabe 7

Erstelle eine Liste mit den Schlüsseln des Dictionaries und eine zweite mit den entsprechenden Werten. Verwende das Muster:

    :::python3
    for key in dictionary:
        print(key, dictionary[key])


Alternativ kannst Du auch mit der Methode `d.items()` alle Schlüssel-Wert-Paare ermitteln.

----

### Aufgabe 8

Plotte die Häufigkeit der Buchstaben als Balkendiagramm.

----

### Aufgabe 9

Zähle die Anzahl der Babys anstatt für jeden Namen nur um 1 hochzuzählen (falls Du nicht schon längst selbst darauf gekommen bist).

----

### Aufgabe 10

Sammle die Buchstabenhäufigkeiten für **alle** Jahrgänge im Dictionary.

Das Dictionary enthält dann für jeden Buchstaben eine Liste, z.B.:

    :::python3
    data = {
        'A': [100, 103, 107, ..],
        'B': [73, 32, 22, ..],
        ..
    }

Normalisiere die Anahl, indem Du durch die Geburtenzahl teilst.

Plotte einige Liniendiagramme, um zu sehen, ob einige Buchstaben mit der Zeit häufiger werden.
