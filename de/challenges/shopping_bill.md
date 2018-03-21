
# Der Einkaufszettel

Dies ist eine 60'-90' lange Einführung für Leute mit Programmiererfahrung.

## Ziele

In dieser Übung wirst Du

1. Ein Python-Programm ausführen.
2. Einfache Ein- und Ausgabefunktionen verwenden.
3. Einfache Datentypen verwenden.
4. `for`-Schleifen und Verzweigungen mit `if` verwenden.
5. Code modularisieren.

## Vorbereitungen

* Lade die [Zip-Datei mit Codebeispielen](http://www.academis.eu/posts/files/python_shopping_list.zip) herunter.
* Finde eine Kurzreferenz zu Python 3.
* Installiere [Python3](http://www.python.org).
* Stelle sicher, dass Du Python über die Kommandozeile mit `python` aufrufen kannst. Du solltest in diesem Fall denPrompt `>>>` sehen. Auch eine andere Python-Umgebung ist in Ordnung.
* Öffne einen Texteditor, der die Python-Syntax kennt (Sublime, Atom, IDLE, emacs, Notepad++, Spyder)

## Aufgabenbeschreibung
Du möchtest prüfen, wie viel Geld Du in letzter Zeit für Einkäufe ausgegeben hast. Dazu hast Du alles in eine durch Tabulatoren getrennte Datei geschrieben (siehe `bill.txt`): 

| Gegenstand | Preis |
|------|-------|
| Tomaten | 4 |
| Kartoffeln | 5 |
| Pizza | 17 |
| Tomaten | 3 |
| Kaffee | 5 |
| Tomaten | 7 |
| Brot | 4 |
| Kaffee | 5 |
| Tomaten | 2 |
| Kaffee | 5 |

## Übung 1: Aufwärmen

Für welche Sorte Gegenstände wurde am meisten ausgegeben? Wie viel?

Schreibe Dir die Zahl auf, bevor Du weitermachst.


## Übung 2: Ein Python-Programm ausführen

Öffne das Programm `shopping.py` im Editor. Führe das Programm von der Kommandozeile aus, indem Du eingibst:

    python shopping.py


### Aufgabe 1.1
Stelle sicher, dass das Programm und Du zum gleichen Ergebnis gelangen.

## Übung 2: Die Funktion print

Schaue Dir im Referenzteil Beispiele für den `print`-Befehl an.

### Aufgabe 2.1
Schreibe ein *“hello world”*-Programm in Python.

### Aufgabe 2.2
Füge `print`-Befvehle zum Programm `shopping.py` hinzu, um die Werte von Variablen anzuzeigen. Führe das Programm aus und stelle sicher, dass es funktioniert.

## Übung 3: Datentypen in Python

### Aufgabe 3.1
Schwreibe ein Programm, das zwei Zahlen von der Tastatur einliest, in Gleitkommazahlen umwandelt und deren Summe ausgibt. Dazu benötigst Du die Funktionen `float()` und `input()`, die im Referenzteil erläutert sind.

### Aufgabe 3.2
Welcher der folgenden Datentypen kommt im Programm `shopping.py` **nicht** vor? 

* list
* string
* float
* dictionary
* integer

## Übung 4: Listen
Für diese Übung benötigst du das Kapitel über Listen und eingebaute Funktionen aus dem Referenzteil.

### Aufgabe 4.1
Schreibe ein Programm, das mit Hilfe der Funktion `range()` eine Liste mit den Zahlen von 1 to 10 erzeugt. Gib die ersten fünf Zahlen der List aus.

### Aufgabe 4.2
Schreibe eine `for`-Schleife, die jede Zahl aus dieser Liste ausgibt.

### Aufgabe 4.3
Füge am Ende von `shopping.py` eine `for`-Schleife hinzu, die die Zwischensumme Zeile für Zeile berechnet und ausgibt.

## Übung 5: Verzweigungen

### Aufgabe 5.1
Füge eine `if`-Anweisung zur `for`-Schleife aus **Aufgabe 4.2** hinzu, um nur die geraden Zahlen auszugeben (`2, 4, 6, ..`).

### Aufgabe 5.2
Ändere `shopping.py` so ab, dass nur jede zweite Zeile aus der Datei ausgegeben wird.

## Übung 6: Dictionaries

### Aufgabe 6.1
Sortiere die Zeilen in `dictionary_example.py`, so dass das Programm ausführbar ist.

### Aufgabe 6.2

| Gegenstand | Preis |
| Tomaten | 6 | 
| Fahrrad | 300 | 
| Busfahrkarte | 2 |

Füge einige Codezeilen zu `shopping.py` hinzu, so dass nach dem Einlesen der Datei noch die drei Gegenstände aus der Tabelle hinzugefügt werden. **Ändere die Textdatei `bill.txt` dazu nicht**:

## Übung 7: Funktionen

### Aufgabe 7.1
Sieh Dir das Programm `function_example.py` an. Ändere das Programm `shopping.py` so ab, dass es das gleiche tut, aber zwei Funktionen verwendet:

* **parse_items** – erhält einen Dateinamen als Parameter und gibt eine Liste von Paaren `(Gegenstand, Wert)` zurück.
* **calc_max3** – Erhält eine Liste von Paaren von `(Gegenstand, Wert)` und gibt die drei Kategorien mit der höchsten Summe zurück.

## Übung 8: Klassen

### Aufgabe 8.1
Schaue Dir das Programm `class_example.py` an. Ändere das Programm `shopping.py` so ab, dass es das gleiche tut, aber dazu eine Klasse `MaxItemsCalculator` verwendet. Diese Klasse soll die Funktionen aus der vorigen Übung als Methoden enthalten. Verwende ein Attribut der Instanz `self`, um das Ergebnis in der Klasse zu speichern.

## Übung 9: Module importieren

### Aufgabe 9.1
Führe das Programm `import_example.py` aus, das die Klasse `MaxItemsCalculator` verwendet. Sorge dafür, dass es funktioniert.
