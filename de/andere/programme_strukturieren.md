
# Programme strukturieren

## Funktionen

### Aufgabe 1

In Python 3.5 gibt es 72 eingebaute Funktionen. Um nützliche Programme zu schreiben, genügt es etwa 25 davon zu kennen. Viele dieser Funktionen sind nützliche Abkürzungen, die Programmzeilen einsparen helfen.

Sammle möglichst viele Funktionen, die Du bereits kennst.


### Aufgabe 2

Jede Python-Datei (mit der Endung .py) kann aus anderen Python-Programmen importiert werden. Jede importierte Python-Datei wird auch **Modul** genannt.

Schreibe ein eigenes Modul und importiere es aus einem eigenen Programm.

### Aufgabe 3

Lies ein größeres Textdokument in die variable `text` ein. Verwende den folgenden Zweizeiler um vierbuchstabige Wörter mit `A` zu finden.

    import re
    re.findall('(a\w\w\w)[^\w]', s, re.IGNORECASE)

### Aufgabe 4

Was haben diese vier Bilder gemeinsam?

![King Kong Flip Flop Hip Hop Ping Pong](regex.jpg)

Bildquellen (links oben nach rechts unten):

* *[By Source (WP:NFCC#4), Fair use](https://en.wikipedia.org/w/index.php?curid=48711736)*
* *[Die Autorenschaft wurde nicht in einer maschinell lesbaren Form angegeben. Es wird Swarve~commonswiki als Autor angenommen, CC BY-SA 3.0](https://commons.wikimedia.org/w/index.php?curid=336076)*
* *[Gaël Marziou from Grenoble, France - IMG_6266_DXO, CC BY 2.0](https://commons.wikimedia.org/w/index.php?curid=47416377)*
* *Derfu, CC BY-SA 3.0*

### Aufgabe 5

Erkläre, was der folgende Codeschnipsel mit dem Bild zu tun hat.

    import re
    text = input()
    if re.search(r"^(\w+)i(\w+)[- ]\1o\2", text):
        print("passt!")


### Aufgabe 6

Wenn das vorige Beispiel zu kompliziert erscheint, versuche es mal mit Telefonnummern mit Vorwahl nach Deutschland:

    print(re.search(r"(00|0 0|\+)\s*4\s*9[0-9 ]+", text))


### Aufgabe 7

Führe die Übung zum ebook **Python 3 Module Examples** unter [https://www.gitbook.com/book/krother/python-3-module-examples/details](https://www.gitbook.com/book/krother/python-3-module-examples/details) durch.

