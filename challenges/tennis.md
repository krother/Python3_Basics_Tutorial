
# Tennis

**🎯 Schreibe eine Klasse `TennisSpiel`, die den Spielstand bei einer Runde Tennis ermittelt.**

* Der Spielstand soll von der Methode `get_score()` ls String berechnet werden
* Der Schiedsrichter ruft entweder `punkt('spieler1')` oder  `punkt('spieler2')` auf

Verwende folgende Grundstruktur:

    class TennisSpiel:

        def __init__(self):
            self.punktestand = {'player1': 0, 'player2': 0}

        def punkt(self, spieler):
            """mit 'spieler1' oder 'spieler2' aufgerufen"""
            self.scores[player] += 1

        def get_score(self):
            ...

## Regeln

1. Der erste Spieler mit mindestens vier Punkten und zwei Punkten mehr als der Gegner gewinnt. Der Punktestand ist dann *"Sieg Spieler 1"* oder *"Sieg Spieler 2"*.
2. Der aktuelle Spielstand beim Tennis ist etwas eigentümlich: Punkte von 0 bis 3 werden mit *"love", "fifteen", "thirty" und "forty"* beschrieben.
3. Wenn beide Spieler mindestens drei Punkte haben, ist der Spielstand bei Gleichstand *"deuce"*.
4. Wenn beide Spieler mindestens drei Punkte haben, ist der Spielstand je nach Spieler mit Mehr Punkten *"Vorteil Spieler 1"* oder *"Vorteil Spieler 2"*
