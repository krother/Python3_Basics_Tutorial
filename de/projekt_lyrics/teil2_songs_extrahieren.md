
# Teil 2: Songs auslesen

## Aufgabe 2.1

Erstelle eine neue Python-Datei `songs_auslesen.py`.

## Aufgabe 2.2

Lies die in Aufgabe 1.4 gespeicherte HTML-Datei ein.

## Aufgabe 2.3

Betrachte die HTML-Datei in einem Texteditor. Finde heraus, wo in der Datei die Songtitel und Links in der Seite sind und woran das Programm diese Stellen erkennen kann.

## Aufgabe 2.4

Schreibe ein Programm, das alle Links zu songs aus der Seite ausliest und in einer Liste sammelt, z.B.:

    [
     'madonna/frozen.html',
     'madonna/burningup.html',
     ..
    ]

Mögliche Ansätze:

* `string.find`
* `string.split`
* Position im String (falls sie immer die gleiche ist)
* Reguläre Ausdrücke

#### Hinweis:

Wenn in der Seite bestimmte Sonderzeichen vorkommen, mußt Du die Datei öffnen mit:

    f = open(dateiname, 'r', encoding='utf-8')

## Aufgabe 2.5

Gib alle Links auf dem Bildschirm aus und prüfe nach, ob das Programm korrekt arbeitet.

## Aufgabe 2.6

Verpacke den bisher geschriebenen Code in eine Funktion:

    def titel_auslesen(dateiname):
        # Dein Code kommt hierhin
        return songtitel

Rufe die Funktion im Programm aus und stelle sicher, daß es immer noch funktioniert.

