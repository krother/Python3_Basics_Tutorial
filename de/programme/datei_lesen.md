
# Textdateien einlesen

### Aufgabe 1

Erstelle eine Textdatei namens `bigbang.txt` für die folgenden Übungen. Fülle sie mit diesen Namen:

    Emily,F,12562
    Amy,F,2178
    Penny,F,342
    Bernadette,F,129
    Leonard,M,384
    Howard,M,208
    Sheldon,M,164
    Stuart,M,82
    Raj,M,41


### Aufgabe 2

Bringe das Programm zum Laufen, indem Du `close`, `line`, `bigbang.txt` und `print` in die Lücken einsetzt.

    f = open(___)
    for ____ in f:
        ____(line)
    f.____()


#### ACHTUNG: 

Je nachdem was für einen Editor Du verwendest, mußt Du eventuell den kompletten Pfad (Verzeichnisnamen) zur Datei eingeben. Wenn Du Dich wunderst, daß das Programm *immer noch nicht* funktioniert, ist die wahrscheinlichste Ursache ein falscher Dateipfad oder Dateiname.


### Aufgabe 3

Schreie ein Programm, welches die Gesamtzahl der Namen (nicht Kinder) in der Datei `bigbang.txt` ermittelt.

Du kannst dazu eine Zählervariable verwenden. Die folgenden zwei Zeilen könnten nützlich sein:

    namen = 0

and 

    namen = namen + 1


### Aufgabe 4

Erstelle eine neue Datei `bigbang_anzahl.txt` und ermittle die Summe der Zahlen. Befülle die Datei mit folgenden Daten:

    12562
    2178
    342
    129
    384
    208
    164
    82
    41


### Aufgabe 5

Berechne die durchschnittliche Anzahl aus der Datei `bigbang_anzahl.txt`.

### Aufgabe 6

Berechne die Standardabweichung aus der Datei `bigbang_anzahl.txt`. Verwende folgenden Codeschnipsel:

    import math
    wurzel = math.sqrt(wert)


### Aufgabe 7

Schreibe ein Programm, welches die dritte Spalte aus der Datei `bigbang.txt` aufsummiert.

#### Hinweis:

Für die Bearbeitung dieser Aufgabe brauchst Du die Funktionen aus der Übung zu Strings.
