
# Einen Webserver mit Flask bauen

In diesem Tutorial kannst Du eine eigene dynamische HTML-Seite erstellen und auf einem Webserver zum Laufen bringen. Wir verwenden dazu das Python-Modul `flask`.

[`flask`](http://flask.pocoo.org/) ist vor allem für kleinere Webseiten geeignet. Eine Alternative ist `Django`, zu dem es das ausgezeichnete [DjangoGirls Tutorial](https://tutorial.djangogirls.org/) gibt.

## 1. Flask installieren

Installiere das Python-Modul `flask` mit `pip`:

    pip install flask

## 2. Eine minimale Webseite starten

Erstelle ein Python-Programm `server.py`, und baue das Hello-World-Beispiel aus der [Flask-Dokumentation](http://flask.pocoo.org/docs/) nach.

Füge folgende Zeile zum Programm hinzu (funktioniert mit Anaconda besser als die in der Dokumentation angegebene Methode):

    app.run()

Starte das Programm. Finde heraus, unter welcher HTTP-Adresse der Server läuft. Setze diese Adresse im Browser ein und prüfe, ob Dein Server erreichbar ist.

#### Tip:

Wir werden den Server im Verlauf des Tutorials noch sehr oft starten müssen. Stelle sicher, dass Du das Programm aus Deinem Editor oder von der Kommandozeile leicht anhalten und neu starten kannst.


## 3. HTML-Code einbinden

Die Flask-Funktionen können HTML-Code zurückgeben. Dies geht z.B. als String mit dreifachen Anführungszeichen. Folgender HTML-Code erzeugt eine Überschrift:

    <h1>Unser Strassenverzeichnis</h1>

Mehr zu HTML-Elementen erfährst Du auf [Selfhtml.org](https://selfhtml.org/).

Baue die Überschrift in die Rückgabe der Python-Funktion ein. Starte den Server neu. Lade die Webseite im Browser neu. Prüfe, ob Deine Überschrift auf der Seite erscheint.

## 4. Eine Unterseite hinzufügen

Schreibe eine zweite Python-Funktion, die den Namen Deiner Strasse ausgibt. Verwende den Dekorator `@app.route`, um die Seite auf die URL `/zuhause` zu legen.

Starte den Server neu und rufe beide Unterseiten im Browser auf (`/` und `/zuhause`).

#### Hilfe:
In der Dokumentation unter [**Routing**](http://flask.pocoo.org/docs/quickstart/#routing)

## 5. Hyperlinks

Erstelle auf der Startseite einen Hyperlink, der auf die Unterseite verweist.

Dazu muss die Funktion `hello()` folgenden HTML-Code zurückgeben:

    <a href="/zuhause">Meine Strasse anzeigen</a>

Starte den Server neu und prüfe, ob der Link funktioniert.

## 6. Ein Template hinzufügen

Es wird schnell beschwerlich, eine ganze HTML-Seite in unser Python-Skript zu kleben. Es ist besser, den HTML-Code in **Templates** zu speichern und diese einzubinden.

Erstelle eine Datei `templates/hello.html`, in die Du den folgenden HTML-Code einfügst:

    <html>
      <head><title>Unser Strassenverzeichnis</title></head>
      <body>
        <h1>Unser Strassenverzeichnis</h1>
        <a href="/zuhause">Meine Strasse anzeigen</a>
      </body>
    </html>  

Binde das Template entsprechend dem Abschnitt [Rendering Templates](http://flask.pocoo.org/docs/quickstart/#rendering-templates) aus der Flask-Dokumentation hinzu.

Starte dann den Server neu und stelle sicher, dass der Inhalt des Templates angezeigt wird (**achte auf die Titelzeile des Browserfensters!**).

## 7. Variablen ins Template einbinden

Wir können aus den Python-Funktionen Daten an ein Template schicken, indem wir ein Dictionary zurückgeben:

    return {'text': "Hallo" }

In den HTML-Templates kannst Du diese Variablen folgendermassen ansprechen:

    {{ !text }}

## 8. Dynamische URLs

Du kannst in den URLs Platzhalter verwenden, deren Inhalt als Variable verfügbar ist. Schreibe eine Funktion, die einen Strassennamen in der URL erhält:

    @app.route('/strasse/<strassenname>')
    def strasse_anzeigen(strassenname):
        ...

Schreibe diese Funktion fertig und probiere die fertige Seite mit unterschiedlichen Strassennamen aus.

#### Achtung:

Mit Platzhaltern kann es leicht passieren, dass zwei Funktionen die gleiche URL ansprechen. Dies kann zu interessanten Fehlern führen, weil nicht sofort ersichtlich ist, welche Funktion Flask aufruft.

## 9. Geodaten bereitstellen

Als Datensatz verwenden wir das [Strassennamenverzeichnis der Zeit](http://www.zeit.de/interactive/strassennamen/). Die Daten liegen ursprünglich im Format **GeoJSON** vor. Wir verwenden eine Datei, die in das `.csv`-Format umgewandelt wurde, so dass Du es bequem mit `pandas` verwenden kannst.

Wähle einige Strassen aus der Datei aus und stelle diese auf der Webseite als Tabelle dar. Lies dazu nach, wie Du eine `for`-Schleife im Template unterbringst.


## 10. Ein Formular erstellen

Erstelle ein Formular mit Flask. Baue ein Formular ein, in dem Du einen Strassennamen in ein Eingabefeld eingibst und über einen Knopf das Formular abschickst. Der HTML-Code sollte etwa folgendes enthalten:

    <form action="/suchen">
      <input name="suchtext"></input>
      <input type="submit" value="Strasse suchen"></input>
    </form>

Die URL `/suchen` kann nun auf den Inhalt des Textfeldes mit dem Namen `suchtext` zugreifen:

    from flask import request

    # in der aufgerufenen Funktion
    text = request.args.get('suchtext')

## 11. Suchergebnisse anzeigen

Verbinde die das Suchergebnis so mit den Daten, dass z.B. eine Tabelle angezeigt wird.

## 12. CSS-Stylesheets einbinden
Nun legen wir Typographie und Farben fest. Lege dazu eine Datei `static/style.css` an. In die Datei schreibst Du Anweisungen, die z.B. die Hintergrundfarbe für das `<body>`-Tag setzen.

    body {
        background-color: lightblue;
    }

Im Header-Teil des HTML-Templates mußt Du das CSS-Stylesheet einbinden:

    <link rel="stylesheet" href="/static/style.css">

## 13. Bootstrap

*"Half the internet is built on Bootstrap"*

**Bootstrap** ist eine Sammlung nützlicher CSS- und JavaScript-Elemente, mit denen Du schnell eine Typographie hinbekommst, die auch auf Mobilgeräten gut aussieht.

Dazu ist eine Reihe von Schritten nötig:

* Binde die Bootstrap-Dateien in Deine Templates ein (siehe [Anleitung](http://getbootstrap.com/docs/4.0/getting-started/introduction/))
* Probiere das *"Starter Template"* aus der Dokumentation aus
* Probiere einzelne Elemente aus (z.B. das [Jumbotron](http://getbootstrap.com/docs/4.0/components/jumbotron/).

#### Anmerkung:

Oft ist es nicht git, Dateien von einer zweiten Webseite einzubinden. Besser ist es, diese als *statische Dateien* auf dem eigenen Server abzulegen.

## 14. Eine Karte mit Folium zeichnen

Stelle die gefundenen Strassen als interaktive Karte dar. 

Dazu musst Du mit der Python-Bibliothek `folium` eine Karte zeichnen und im Verzeichnis `templates/` speichern, z.B. als `templates/karte.html`.

Dies kannst Du in einem Template einbinden:

    {% 'karte.html' %}



## Erweiterungsmöglichkeiten

* **Eine SQL-Datenbank verwenden** – Anstatt bei jedem Neustart des Servers 900 MB Daten in den Speicher zu laden, kannst Du mit dem Python-Modul `sqlite3` eine Datenbank erstellen und die gewünschten Strassen aus einer Tabelle abfragen.
* **Deployment auf einem öffentlichen Server** – Auf [pythonanywhere](https://www.pythonanywhere.com/) kannst Du Deinen eigenen Server anlegen. Probiere es aus! Es kostet nichts.
* **git** – mit `git` kannst Du Deinen Code veröffentlichen. Dadurch werden viele andere Schritte deutlich einfacher.
* Im [**Djangogirls-Tutorial**](https://tutorial.djangogirls.org/en/deploy/) findest Du eine ausführliche Anleitung für diese Schritte mit dem Python-Server `Django`.
