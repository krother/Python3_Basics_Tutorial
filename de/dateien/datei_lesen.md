
# Textdateien einlesen

### Aufgabe 1

Erstelle in einem Texteditor eine Datei namens `bigbang.txt`. Fülle sie mit folgenden Daten:

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

Bringe das Programm zum Laufen, indem Du `close`, `line`, `"bigbang.txt"` und `print` in die Lücken einsetzt.

    f = open(___)
    for ____ in f:
        ____(line)
    f.____()


#### ACHTUNG: 

Je nachdem was für einen Editor Du verwendest, mußt Du eventuell den kompletten Pfad (Verzeichnisnamen) zur Datei eingeben. Wenn Du Dich wunderst, daß das Programm *immer noch nicht* funktioniert, ist die wahrscheinlichste Ursache ein falscher Dateipfad oder Dateiname.



### Aufgabe 3

Wie viele unterschiedliche *Mädchennamen* mit `'B'` gab es 2015?

**Sortiere** die folgenden Programmzeilen und **rücke sie korrekt ein**:

    girls = 0

    if "B" in line:

    print(girls)

    if ",F," in line:

    for line in open('names/yob2015.txt'):

    girls += 1


### Aufgabe 4

Erweitere das Programm aus der vorigen Aufgabe so, daß die Anzahl der Jungen- und Mädchennamen getrennt gezählt und ausgegeben werden.


### Aufgabe 5

Welche der folgenden Befehle sind korrekt?

* `for char in "ABCD":`
* `for i in range(10):`
* `for number in [4, 6, 8]:`
* `for k in 3+7:`
* `for (i=0; i<10; i++):`
* `for var in open('bigbang.txt'):`


### Aufgabe 6

Schreibe ein Programm, das die Zeilen aus der Datei `yob2015.txt` einliest. Finde alle Zeilen, die Deinen Namen enthalten und gib diese auf dem Bildschirm aus.



