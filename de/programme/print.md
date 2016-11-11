
# Ausgabe auf den Bildschirm

In diesem Abschnitt werden wir unserer erstes Python-Programm schreiben. Es wird ein sehr einfaches Programm sein, welches einfach einige Namen von Babys auf den Bildschrim schreibt.


### Aufgabe 1

Öffne einen Texteditor (also *keine IPython-Konsole*) und erstelle eine leere Datei. Schreibe hinein: 

    print("Hannah")
    print(23073)

Speichere die Datei anschließend unter dem Namen `ausgabe.py` ab.

### Aufgabe 2

Nun werden wir das Programm ausführen.

* Unter **Anaconda** und **Canopy** können wir das mit dem *"Play"*-Knopf tun.
* In **IDLE** erreichen wir das gleiche durch Drücken von `F5`.
* Unter **Unix** öffnen wir ein Terminal (ohne IPython), wechseln in das Verzeichnis mit der Datei `ausgabe.py` und schreiben:

    python3 ausgabe.py


### Aufgabe 3

Erkläre das folgende Programm:

    name = "Emily"
    jahr = 2000
    print(name, jahr)


### Aufgabe 4

Schreibe in ein **Programm** (eine Datei mit der Endung `.py`):

    name = "Emily"
    name

Was passiert, wenn Du das Programm ausführst?


### Aufgabe 5

Welche `print`-Anweisungen sind korrekt?

* `print("9" + "9")`
* `print "nine"`
* `print(str(9) + "nine")`
* `print(9 + 9)`
* `print(nine)`


### Aufgabe 6

Erkläre die folgende Anweisung:

    print("Emily\tSmith\n2000")

### Aufgabe 7

Manche Babys haben berühmte Namensvettern. Schreibe ein Programm, welches folgende Ausgabe produziert:

    Harry      Hermione      Severus
    Tyrion     Daenerys      Frodo
    Luke       Leia          Darth

### Aufgabe 8

Erschwere Dir die vorige Aufgabe, indem Du:

* die Ausgabe mit einem einzigen `print`-Befehl erzeugst.
* die Namen vorher in Variablen speicherst.
