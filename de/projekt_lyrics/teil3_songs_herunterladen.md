
# Teil 3: Songtexte herunterladen

## Aufgabe 3.1

Erstelle Dir ein Verzeichnis, in dem Du die Songtexte speichern möchtest.

## Aufgabe 3.2

Lösche sämtliche Leer- und Sonderzeichen aus dem Songtitel, um einen Dateinamen zu erhalten.

Füge dem Dateinamen als Endung `.html` hinzu.

## Aufgabe 3.3

Nimm **nur den ersten Song der Liste**. Erstelle aus dem Link zu diesem Song eine vollständige URL. 


## Aufgabe 3.4

Lade einen *einzelnen* Song herunter und speichere diesen in einer Textdatei.

## Aufgabe 3.5

Verpacke das Herunterladen eines Songs in einer Funktion:

    def song_herunterladen(titel, link):
        # Dein Code hierhin

Verwende wie in Aufgabe 1 die `headers`, um einen Browser zu simulieren.

## Aufgabe 3.6

Verwende das Modul `time`, um nach dem Herunterladen und Speichern eines Songs 120 Sekunden zu warten:

    import time
    time.sleep(120)

**DIES IST DER WICHTIGSTE SCHRITT IN DER HEUTIGEN AUFGABE. WENN EINER VON UNS DIESEN VERGISST, KANN ES GANZ LEICHT PASSIEREN, DASS DER SERVER DIE GANZE KLASSE AUSSPERRT.**

## Aufgabe 3.7

Verwende die Funktion `song_herunterladen`, um **die ersten 20 Songs** herunterzuladen.

## Aufgabe 3.8

Prüfe vor dem Herunterladen, ob eine Datei schon existiert:

    import os
    if os.path.exists()

Lade nur Dateien herunter, die es noch nicht gibt.
