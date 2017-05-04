
# Verschachtelte Listen

Daten treten häufig in Form von Tabellen auf. Um Tabellen in Python zu verarbeiten, kommt uns entgegen, daß wir Listen in anderen Listen speichern können. Damit sieht eine einfache Tabelle in Python so aus:

    # Spalten: Name, #California, #New York
    [
      ["Emily", 2269, 881],
      ["Amy", 542, 179],
      ["Penny", 54, 12],
      ["Bernadette", 21, 11]
    ]


Diese Art von Tabelle nennt man auch *verschachtelte Liste*.

In diesem Teil des Kurses werden wir uns mit Aufbau und Verarbeitung von verschachtelten Listen beschäftigen.


### Aufgabe 1

Gib alle Zeilen der obigen Tabelle mit einer `for`-Schleife aus.


### Aufgabe 2

Gib alle *Zellen* der obigen Tabelle mit einer *doppelten* `for`-Schleife aus.


### Aufgabe 3

Erzeuge eine Tabelle mit 10x10 Zellen und fülle sie mit den Zahlen von 1 bis 100.


### Aufgabe 4

Sortiere die obige Tabelle nach der zweiten Spalte. Der folgende Codeschnipsel könnte dabei nützlich sein:

    from operator import itemgetter
    tabelle.sort(key=itemgetter(spaltennr))
