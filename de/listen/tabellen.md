
# Verschachtelte Listen

Daten treten häufig in Form von Tabellen auf. Um Tabellen in Python zu verarbeiten, kommt uns entgegen, daß wir Listen in anderen Listen speichern können. Damit sieht eine einfache Tabelle in Python so aus:

    [
     ["Penny", 123],
     ["Sheldon", 456]
    ]

Diese Art von Tabelle nennt man auch *verschachtelte Liste*.

In diesem Teil des Kurses werden wir uns mit Aufbau und Verarbeitung von verschachtelten Listen beschäftigen.


### Aufgabe 1

Erzeuge eine leere Tabelle mit 10x10 Zellen, die alle die Zahl `0` enthalten.

### Aufgabe 2

Fülle die gleiche Tabelle mit den Zahlen von 1 bis 100.


### Aufgabe 3

Lies die Anzahlen von Babynamen aus der Datei für das Jahr 2000 ein. Speichere alle Namen, Geschlechter und Werte in einer Liste. Gib die ersten 10 Zeilen der Tabelle aus.


### Aufgabe 4

Bilde aus der Liste die Summe der Geburten insgesamt. Vergleiche den Wert für das Jahr 2000 mit dem für 1900.


### Aufgabe 5

Sortiere die Tabelle für das Jahr 2000 nach der Spalte *Anzahl*. Der folgende Codeschnipsel könnte dabei nützlich sein:

    from operator import itemgetter
    tabelle.sort(key=itemgetter(spaltennr))
