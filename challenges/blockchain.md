
# Blockchain

**🎯 Implementiere Deinen eigenen Blockchain-Algorithmus.**

## Schritt 1

Schreibe eine Funktion, die zufällige Transaktionen im Format `(name1, name2, betrag)` generiert.

Wir möchten diese Transaktionen *fälschungssicher* speichern, also so,  dass sie nachträglich möglichst schwer zu manipulieren sind.

## Schritt 2

Definiere einen Datentyp *"Block"*, der folgendes enthält:

* Den Hash eines vorhergehenden Blocks
* Einige Transaktionen
* Eine Prüfsumme (eine beliebige Zahl oder einen String)

## Schritt 3

Schreibe eine Funktion, die aus allen Eigenschaften eines Blocks einen Hash berechnet. Repräsentiere dazu den gesamten Block als String. Verwende die Hash-Funktion `sha256`:

    import hashlib

    h = hashlib.sha256()
    h.update(text.encode())
    print(h.hexdigest())

## Schritt 4

Lege die Blockchain als leere Liste an.

Erzeuge den ersten Block, den "Genesis-Block". Verwende 'genesis' als vorangegangenen Hash. Plaziere einige zufällige Transaktionen im Block.

Finde eine Prüfsumme, so dass der *sha256-hexdigest* mit vier Nullen (`0000`) endet. Du musst eventuell viele Prüfsummen ausprobieren.

Füge den fertigen Block an die Blockchain an.

## Schritt 5

Erzeuge den zweiten Block:

* Der Hash ist der `hexdigest` des vorangegangenen Blocks
* Füge weitere Transaktionen hinzu.
* Finde wieder eine Prüfsumme, die einen `hexdigest` mit vier Nullen am Ende erzeugt.
* Füge den fertigen Block der Blockchain hinzu.

## Schritt 6

Erzeuge weitere Blöcke.

## Fragen

* Was passiert, wenn die Anzahl notwendiger Nullen im Hexdigest auf 2 oder 6 gesetzt wird?
* Was passiert, wenn jemand eine Transaktion im Genesis-Block verändert?
* Wodurch wird die Blockchain fälschungssicher?
* Wie ließe sich eine Blockchain dennoch fälschen?
* Warum nennt man das Finden der Prüfsumme auch *"proof of work"*?
* Warum sind in einer Blockchain mehrere Rechner beteiligt?
* Was ist ein *"Konsens-Algorithmus"?
