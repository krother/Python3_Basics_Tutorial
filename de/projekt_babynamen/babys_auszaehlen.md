
# Babynamen auszählen

In diesem Kapitel werden wir einen größeren String auseinandernehmen. Dies kommt beim Analysieren von Daten immer wieder vor. Zum Üben verwenden wir folgenden mehrzeiligen String (die Daten sind ein Auszug aus dem US-Geburtenregister):

    bigbang = """Emily,F,12562
    Amy,F,2178
    Penny,F,342
    Bernadette,F,129
    Leonard,M,384
    Howard,M,208
    Sheldon,M,164
    Stuart,M,82
    Raj,M,41"""

Wir werden ausrechnen, wie viele Babys die Tabelle insgesamt enthält.

### Aufgabe 1

Wenn alle Zahlen in einer Liste wären, wäre es einfach:

    bigbang_zahlen = [
        12562, 2178, 342, 129,
        384, 208, 164, 82, 41
    ]

Schreibe ein Programm, das diese Zahlen aufsummiert.

----

## Methoden von Strings

### Aufgabe 2

Um statt Zahlen den Text in `bigbang` zu verarbeiten, müssen wir den Datentyp **String** etwas besser kennen lernen.

Finde heraus, was die Ausdrücke mit dem String in der Mitte tun.

![string exercise](../exercises/strings.png)


### Aufgabe 3

<quiz name="">
    <question>
        <p>Mit welcher der Methoden kannst du einen String wie die Variable <code>bigbang</code> in einzelne Zeilen zerlegen?</p>
        <answer><code>bigbang.replace(x, y)</code></answer>
        <answer correct><code>bigbang.split(x)</code></answer>
        <answer><code>bigbang.strip()</code></answer>
        <answer><code>bigbang.count(x)</code></answer>
        <explanation>Die Methode <code>str.split()</code> zerlegt einen String in eine Liste von Teilstrings. Du kannst als Argument in den Klammern angeben, bei welchem Zeichen zerteilt werden soll. Voreingestellt sind Leerzeichen, Tabulator und Zeilenumbruch.</explanation>
    </question>
</quiz>

### Aufgabe 4

Nun wenden wir diese Methode an. Schreibe ein Programm, das *eine Zeile* aus unserem Datensatz zerlegt und den Namen und die korrekte Anzahl ausgibt:

    zeile = "Emily,F,12562"

Probiere aus, ob das gleiche Programm auch für letzte Zeile funktioniert.

    zeile = "Raj,M,41"

<!--sec data-title="Hinweis" data-id="hint-zeile-zerlegen"
data-collapse=true ces-->

Bei der Methode `bigbang.split()` kannst Du in den Klammern angeben, bei welchem Zeichen getrennt werden soll. Speichere das Ergebnis in einer Variablen. Mit eckigen Klammern (Index) kannst Du aus der Liste ein Element auswählen.

<!--endsec-->

### Aufgabe 5

Nun probiere, den gesamten String `bigbang` zu zerlegen. Zerlege dann die 5. Zeile und gib die Anzahl aus.


### Aufgabe 6

Da wir nicht eine, sondern *alle* Zeilen verarbeiten möchten, müssen wir Befehle wiederholen. Du denkst Dir vielleicht schon, dass dazu eine `for`-Schleife nützlich sein kann.

Schreibe ein Programm, das alle Namen aus der Variable `bigbang` ausgibt.

<!--sec data-title="Hinweis" data-id="hint-for-bigbang"
data-collapse=true ces-->

Du kannst das Ergebnis von `bigbang.split()` direkt an die `for`-Schleife anhängen:

    for zeile in bigbang.split():
        ...

<!--endsec-->

### Aufgabe 7

Wie viele unterschiedliche Jungennamen mit `'S'` gab es 2015?

**Sortiere** die folgenden Programmzeilen und **rücke sie korrekt ein**:

    jungs = 0

    if "B" in zeile:

    print(jungs)

    if ",M," in zeile and zeile[0] == 'S':

    for zeile in bigbang.split():

    jungs += 1


### Aufgabe 8 

Nun haben wir es fast geschafft. Ein Detail fehlt aber noch: **Typumwandlungen**.

Wenn Du statt einer Liste von Zahlen Strings aufsummieren möchtest, erhälst Du ein seltsames Ergebnis oder eine Fehlermeldung. Wir müssen die Strings zunächst in **int** oder **float** umwandeln.

Python enthält viele Funktionen zur **Umwandlung von Datentypen**. Setze die folgenden Teile in den Code ein, so dass alle Befehle korrekt ausgeführt werden: `alter`, `int(alter)`, `name`, `str(geboren)`, `1980`

    name = 'Sheldon Cooper'
    geboren = _____
    ____ = '38'

    text = ____ + ' kam im Jahr ' + _____ + ' zur Welt.'
    jahr = geboren + _____
    print(text)
    print(jahr)


### Aufgabe 9

Ergänze die folgenden Anweisungen durch `int()` oder `str()`, so daß sie alle funktionieren.

    9 + 9
    9 + '9'
    '9' + '9'
    9 * '9'


### Aufgabe 10

Schreibe ein Programm, das die Anzahl der Babys in der Variable `bigbang` zusammenzählt und die Summe ausgibt.
