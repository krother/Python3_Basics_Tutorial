
# Textdateien einlesen

### Aufgabe 1

Erstelle eine Textdatei namens `bigbang.txt` für die folgenden Übungen. Fülle sie mit diesen Daten:

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

Schreibe ein Programm, welches die Gesamtzahl der Namen (nicht Kinder) in der Datei `bigbang.txt` ermittelt.

Du kannst dazu eine Zählervariable verwenden. Die folgenden zwei Zeilen könnten dabei nützlich sein:

    namen = 0

und 

    namen = namen + 1


### Aufgabe 4

Wie viele unterschiedliche *Mädchennamen* mit `'B'` gab es 2015?

**Sortiere** die folgenden Programmzeilen und **rücke sie ein**:

    girls = 0

    if "B" in line:

    print(girls)

    if ",F," in line:

    for line in open('names/yob2015.txt'):

    girls += 1

### Aufgabe 5

Führe das folgende Programm aus. Was wird berechnet?

    boys = 0
    girls = 0
    for line in open('names/yob2015.txt'):
        if ",M," in line:
            boys = boys + 1
        elif ",F," in line:
            girls = girls + 1
        else:
            print("Zeile nicht erkannt:\n", line)
    print(boys, girls)

### Aufgabe 6

Schreibe ein Programm, das die Zeilen aus der Datei `yob2015.txt` einliest. Finde die Zeile(n) die Deinen Namen enthalten und gib diese auf dem Bildschirm aus.
