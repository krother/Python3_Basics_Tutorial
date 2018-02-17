
# Teil 1: Songliste herunterladen

## Aufgabe 1.1

Besuche im Browser die Seite [azlyrics.com](http://www.azlyrics.com). Suche Dir einen beliebigen Interpreten aus (außer **Madonna**, **Eminem** und **Beatles**, die habe ich schon).

Notiere Dir die URL.

## Aufgabe 1.2

Erstelle eine Python-Datei `download.py`.

## Aufgabe 1.3

Verwende das Modul `requests`, um die Seite mit der Songliste des gewählten Interpreten herunterzuladen.

Damit das funktioniert, müssen wir so tun als wäre Python ein Browser. Das geht mit:

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    seite = requests.get(url, headers=headers)

## Aufgabe 1.4

Speichere die heruntergeladene Seite in einer HTML-Datei.

#### Hinweis:

Wenn in der Seite bestimmte Sonderzeichen vorkommen, mußt Du die Datei zum Schreiben öffnen mit:

    f = open(dateiname, 'w', encoding='utf-8')
