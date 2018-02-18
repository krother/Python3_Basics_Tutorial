
# Reguläre Ausdrücke

### Aufgabe 1

Finde Wörter mit `F` im Text. Führe dazu folgendes Beispiel aus:

    import re

    text = "Es war einmal ein Ferkel, das hatte eine Flöte"
    found = re.findall('(F\w+)[^\w]', text, re.IGNORECASE)
    print(found)


### Aufgabe 2

Was haben diese vier Bilder gemeinsam?

![King Kong Flip Flop Hip Hop Ping Pong](regex.jpg)

Bildquellen (links oben nach rechts unten):

* *[By Source (WP:NFCC#4), Fair use](https://en.wikipedia.org/w/index.php?curid=48711736)*
* *[Die Autorenschaft wurde nicht in einer maschinell lesbaren Form angegeben. Es wird Swarve~commonswiki als Autor angenommen, CC BY-SA 3.0](https://commons.wikimedia.org/w/index.php?curid=336076)*
* *[Gaël Marziou from Grenoble, France - IMG_6266_DXO, CC BY 2.0](https://commons.wikimedia.org/w/index.php?curid=47416377)*
* *Derfu, CC BY-SA 3.0*

Führe folgendes Codebeispiel aus:

    import re
    text = input("Was ist auf einem der Bilder zu sehen? ")
    if re.search(r"^(\w+)i(\w+)[- ]\1o\2", text):
        print("stimmt!")

### Aufgabe 3

Besuche die Seite [www.regexone.com](http://www.regexone.com) und führe einige der Übungen aus.

### Aufgabe 4

Schreibe ein Programm, das E-Mail-Adressen in Text erkennt.

Verwende die Funktion `re.findall` und erstelle ein entsprechendes Suchmuster.

Auf [Regex101](https://regex101.com/) kannst Du den regulären Ausdruck testen.
