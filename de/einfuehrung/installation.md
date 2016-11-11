
# Python installieren

Der erste Schritt in die Welt des Programmierens ist, Python auf Deinem Computer zum Laufen zu bringen. Dazu benötigst Du zwei Programme:

* Python 3
* einen Texteditor

Welchen Editor Du installieren solltest, hängt von Deinem Betriebssystem ab.

## Auf Ubuntu Linux

Unter Ubuntu ist Python standardmäßig bereits installiert. Allerdings werden wir in diesem Tutorial nach Möglichkeit **Python 3** verwenden. Du kannst Python 3 über die Kommandozeile mit folgenden Befehlen installieren:

    sudo apt-get install python3
    sudo apt-get install ipython3

Um zu prüfen, ob es funktioniert hat, gib anschließend ein:

    ipython3

Als Texteditor ist für den Anfang **gedit** in Ordnung. In diesem Falle solltest Du jedoch unbedingt Tabulatoren als 4 Leerzeichen belegen. Dies kannst Du im Menü unter *Edit -> Preferences -> Editor -> Häkchen setzen bei 'Insert spaces instead of tabs'*. Ich bevorzuge allerdings den Editor **Sublime 2**, der zusätzliche Optionen für Fortgeschrittene bietet.

## Unter Windows

Ein bequeme Möglichkeit, Python 3, einen Editor und viele Zusatzpakete in einem Rutsch zu installieren, bietet [**Anaconda**](https://store.continuum.io/cshop/anaconda/) -- eine Python-Distribution, die hervorragend für wissenschaftliche Anwendungen geeignet ist.

Halte nach der Installation im Startmenü nach *Python*, *Anaconda* oder *Spyder* im Startmenü Ausschau und klicke Dich durch die Dialogfenster.

## Weitere Python-Distributionen

* [**Python 3**](https://www.python.org/downloads/) - installiert lediglich den Python-Interpreter und einen einfachen Editor (*Idle*).
* [**Canopy**](https://www.enthought.com/products/canopy/) ist wie Anaconda eine Distribution mit vielen Paketen und einem eigenen Editor.

### Weitere Editoren

* **Idle** - ein minimalistischer Editor für Python, der Teil der Standard-Distribution ist
* **Sublime Text 2** - ein sehr mächtiger Texteditor mit konfigurierbaren Sonderfunktionen.
* **PyCharm** - eine professionelle auf Python spezialisierte Entwicklungsumgebung, die zum Entwickeln großer Projekte sehr gut geeignet ist. Du wirst 90% der Funktionen eine lange Zeit lang nicht brauchen, aber es ist ein sehr schönes Programm.
* **Notepad++** - ein sehr nützlicher Editor für Windows. *Bitte verwende auf keinen Fall Notepad, um Python zu programmieren. Du tust Dir keinen Gefallen damit. Du solltest stattdessen lieber versuchen, mit einer Nagelfeile aus dem Gefängnis auszubrechen.*
* **vim** - ein konsolenbasierter Texteditor für Unix. Dies ist das Werkzeug der Wahl für Systemadministratoren und alle Entwickler, die sich oft auf anderen Rechnern einloggen müssen, um dort zu arbeiten.

## Fragen

#### Frage 1

Welche Texteditoren sind auf Deinem System installiert?

#### Frage 2

Welche Python-Version läuft bei Dir?
