
# Antworten auf die Hinweisfragen

## Antwort auf Hinweisfrage 1

Beispielhafte Ausgabe:

    1311   und
     223   prinzessin
     175   sultan


## Antwort auf Hinweisfrage 2

1. Lies die Datei ein
2. Teile sie in Wörter auf
3. Zähle jedes Wort
4. Sortiere die Wörter nach Anzahl
5. Gib die häufigsten Wörter + Anzahlen aus.

## Antwort auf Hinweisfrage 3

Dictionaries sind zum Zählen von Dingen geeignet

## Antwort auf Hinweisfrage 4

Dictionary initialisieren:

    counter = {}


Ein einzelnes Wort zählen:

    counter.setdefault('palast', 0)
    counter['palast'] += 1
    
## Antwort auf Hinweisfrage 5

Lesen einer Textdatei:

    text = open(dateiname).read()
    
Einen String zerteilen:

    woerter = text.split()


## Antwort auf Hinweisfrage 6

Listen in Python lassen sich gut sortieren. 
Listen können Tupel enthalten, z.B.:

    daten = [ (12, 34), (56, 78) ]
    daten.sort()

Versuche die folgenden Listen in der Python Shell zu sortieren:

    [('aaa', 100), ('bbb', 20)]

und

    [(100, 'aaa'), (20, 'bbb')]


## Antwort auf Hinweisfrage 7

Die ersten vier Plätze sollten sein:

    1311     und
     990     die
     968     der
     867     er

## Antwort auf Hinweisfrage 8

Sonderzeichen lassen sich einzeln mit der Funktion `str.replace` entfernen, z.B. `str.replace('.', '')`.

