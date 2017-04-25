
# Wiederholungsübung

### Aufgabe 1

Das folgende Programm sammelt Namen, die mindestens 10000x verwendet wurden in einer Liste. Leider enthält das Programm **vier Fehler**. Finde und korrigiere diese.


    häufige = []

    for line in open('names/yob2015.txt'):
        spalten = line.strip().split(',')
        name = spalten[1]
        anzahl = int(spalten[3])
        if anzahl >= 10000
            häufige.append(name)

    print(haeufige)


### Aufgabe 2

Schreibe ein Programm, das die Datei `bigbang.txt` einliest. Sammle alle Namen in einer Liste. Gib die Liste aus.

Hier ist noch einmal der Inhalt der Datei:

    Emily,F,12562
    Amy,F,2178
    Penny,F,342
    Bernadette,F,129
    Leonard,M,384
    Howard,M,208
    Sheldon,M,164
    Stuart,M,82
    Raj,M,41


### Aufgabe 3

Sammle die Namen der Jungen in einer zweiten Liste. Gib auch diese aus.


### Aufgabe 4

Schreibe ein Programm, welches ermittelt, wie oft Dein eigener Name in den Babynamen Deines Geburtsjahrgangs vorkommt. Gib diese Anzahl aus.


### Aufgabe 5

Welche der folgenden Befehle sind korrekt?

* `for char in "ABCD":`
* `for i in range(10):`
* `for number in [4, 6, 8]:`
* `for k in 3+7:`
* `for (i=0; i<10; i++):`
* `for var in open('bigbang.txt'):`

### Aufgabe 6

Schreibe ein Programm, welches *die drei häufigsten* Vornamen für Jungen und Mädchen in jedem Jahrgang ermittelt und ausgibt.

### Aufgabe 7

Schreibe ein Programm, welches den prozentualen Anteil der 10 häufigsten Namen für das Jahr 2000 berechnet und ausgibt.
