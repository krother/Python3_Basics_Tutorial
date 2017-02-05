
# Reguläre Ausdrücke

### Aufgabe 1

erwende den folgenden Zweizeiler um Wörter mit `F` zu finden.

    import re

    text = "Es war einmal ein Ferkel, das hatte eine Flöte"
    found = re.findall('(a\w+)[^\w]', text, re.IGNORECASE)
    print(found)

### Aufgabe 2

Besuche die Seite [www.regexone.com](http://www.regexone.com) und führe die ersten drei Übungen aus.

### Aufgabe 3

Was haben diese vier Bilder gemeinsam?

![King Kong Flip Flop Hip Hop Ping Pong](regex.jpg)

Bildquellen (links oben nach rechts unten):

* *[By Source (WP:NFCC#4), Fair use](https://en.wikipedia.org/w/index.php?curid=48711736)*
* *[Die Autorenschaft wurde nicht in einer maschinell lesbaren Form angegeben. Es wird Swarve~commonswiki als Autor angenommen, CC BY-SA 3.0](https://commons.wikimedia.org/w/index.php?curid=336076)*
* *[Gaël Marziou from Grenoble, France - IMG_6266_DXO, CC BY 2.0](https://commons.wikimedia.org/w/index.php?curid=47416377)*
* *Derfu, CC BY-SA 3.0*

### Aufgabe 4

Erkläre, was der folgende Codeschnipsel mit dem Bild zu tun hat.

    import re
    text = input()
    if re.search(r"^(\w+)i(\w+)[- ]\1o\2", text):
        print("passt!")

### Aufgabe 5

Schreibe ein Programm, das Telefonnummern mit Vorwahl nach Deutschland erkennt.
Verwende den folgenden regulären Ausdruck:

    re.search(r"(00|0 0|\+)\s*4\s*9[0-9 ]+", text)


