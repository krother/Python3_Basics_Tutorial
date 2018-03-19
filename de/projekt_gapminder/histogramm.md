
# Histogramme plotten

Zeichne ein Histogramm der Lebenserwartung für das Jahr 2015. Da uns `pandas` die meiste Arbeit abnimmt, werden wir die Gelegenheit dazu nutzen, das Diagramm möglichst hübsch zu gestalten.

### Schritt 1

Da die Aufbereitung der Daten sich nicht sonderlich von der letzten Übung unterscheidet, kannst Du die Daten und den Code wiederverwenden.

Sorge dafür, daß Du die Lebenserwartung in einem DataFrame `lifeexp` hast.

### Schritt 2

Wähle einige Jahrgänge aus. Beim Einlesen aus Excel haben die Daten jedoch *Integer-Zahlen* als Spaltennamen. Daher:

    lifeexp = lifeexp[[1950, 1975, 2000, 2015]]

### Schritt 3

Zeichne ein Histogramm für das Jahr 2015 mit den Standardeinstellungen.

    import pylab as plt

    lifeexp[2015].hist()
    plt.savefig('histo.png')

### Schritt 3

Probiere unterschiedliche Werte für die Klassenanzahl aus. Wähle jeweils einen der folgenden Befehle und ersetze den vorher ausgeführten:

    lifeexp['spaltenname'].hist(bins=5)
    lifeexp['spaltenname'].hist(bins=10)
    lifeexp['spaltenname'].hist(bins=20)

Entscheide Dich für einen aussagekräftigen Wert.


### Schritt 4

Nun werden wir das Diagramm verschönern.

Beschrifte das Diagramm. Verwende dazu vor dem Abspeichern die Funktionen:

    plt.title('text')
    plt.xlabel('text')
    plt.ylabel('text')


### Schritt 5

Stelle über die Funktion `plt.axis` den Bildausschnitt ein.

    plt.axis([0.0, 50.0, 0.0, 10.0)

Finde passende Zahlen und setze diese in den obigen Befehl ein.


### Schritt 6

Probiere nacheinander folgende optionale Parameter der Funktion `hist()` aus:

    facecolor='green',
    facecolor='#ff0000',
    alpha=0.75,
    histtype='bar',

Die Parameter werden in den Aufruf von `hist()` am Ende angefügt.

### Schritt 7

Lege die Auflösung beim Schreiben fest.

    plt.savefig('histo.png', dpi=150)

Probiere auch, das Diagramm als SVG-Grafik abzuspeichern, indem Du die Endung `.svg` angibst. Welche Vor- und Nachteile haben die Formate PNG und SVG?

