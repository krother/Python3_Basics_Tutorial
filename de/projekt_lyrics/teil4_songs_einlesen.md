
# Teil 4: Songs einlesen

*Diesen Teil kannst Du bequem bearbeiten, wenn das andere Proramm noch im Hintergrund mit Herunterladen beschäftigt ist.*

## Aufgabe 4.1

Erstelle ein neues Programm `songs_einlesen.py`

## Aufgabe 4.2

Gib die Namen aller Songdateien aus. Verwende das Modul `os`:

    import os
    for dateiname in os.listdir(PFAD):
        print(dateiname)

## Aufgabe 4.3

Betrachte eine Songdatei im Texteditor. Finde heraus, wo der eigentliche Text beginnt und endet.

## Aufgabe 4.4

Lies eine Songdatei als einzelnen String ein. Verwende dazu `read()`:

    text = open(dateiname).read()

Schneide den Songtext aus. Dies geht recht gut mit Hilfe von `text.find()`.

## Aufgabe 4.5

Verpacke das Einlesen eines Songs in eine Funktion, die den Text als String zurückgibt.

## Aufgabe 4.6

Lies alle Songs in eine Liste von Strings ein. Verpacke auch diesen Code in eine Funktion:

    def songtexte_auslesen(verzeichnis):
        # Dein Code
        return textliste

