
# Analyse der letzten Buchstaben

**🎯 Analysiere welche letzten Buchstaben am häufigsten in Vornamen vorkommen.**

## Aufgabe 1

Lies alle Jahrgänge aus dem [Babynamen-Datensatz](http://www.ssa.gov/oact/babynames/limits.html) in ein einzelnes `DataFrame` ein. Das `DataFrame` soll die Spalten **Anzahl**, **Geschlecht**, **Name** und **Jahr** haben. Folgende Codeschnipsel könnten dabei nützlich sein:

    df['jahr'] = 2015

    df = pd.concat([df1, df2, df3, ...])

    for jahr in range(1880, 2015):

    jahrgaenge = []


## Aufgabe 2

Schreibe eine Funktion, die den letzten Buchstaben zurückgibt. Füge dem DataFrame eine neue Spalte mit dem letzten Buchstaben hinzu. Verwende dazu `df.apply`.

## Aufgabe 3

Berechne die Summe der Vornamen nach Geschlecht, Anfangsbuchstabe und Jahr gruppiert. Die resultierende Tabelle sollte etwa so aussehen:

    gender  last  year
    F       a     1880    31446
                  1881    31581
                  1882    36536

Dieses `DataFrame` besitzt einen **hierarchischen Index**.

## Aufgabe 4

Nun müssen wir den **Anteil an den gesamten Vornamen eines Jahrgangs** für Jungen berechnen. Leider sind die drei Befehle dazu durcheinandergekommen. Finde die korrekte Reihenfolge heraus:

    df = df / df.sum()
    df = df.unstack()
    df = df.ix['M']

### Hinweise:

Der Endbuchstabe `a` hatte im Jahr 1880 einen Anteil von 0.007023

## Aufgabe 5

Wähle die Jahrgänge **1910** und **2010** aus. Zeichne ein Balkendiagramm mit je einer Balkengruppe für jeden Buchstaben, bestehend aus zwei Balken für die beiden Jahrgänge.

## Aufgabe 6

Wähle die Endbuchstaben **d**, **n** und **y** aus. Zeichne ein Liniendiagramm, das die Häufigkeit dieser Buchstaben im zeitlichen Verlauf darstellt.

## Aufgabe 7

Wie haben sich die Endbuchstaben im letzten Jahrhundert verändert?

## Aufgabe 8

Ist ein ähnlicher Effekt für Mädchen zu beobachten?
