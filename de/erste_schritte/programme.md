
# Programme in Python schreiben

Mit IPython Anweisungen zu schreiben ist eine Zeitlang ganz nett. Komplexere Programme Befehl für Befehl zu schreiben ist aber auf die Dauer recht beschwerlich. Um wirklich sinnvoll programmieren zu können, müssen wir unsere Anweisungen in **Programmen** speichern, so daß wir sie später beliebig oft **ausführen** können.

Ein Programm besteht aus mehreren Zeilen, die in einem Rutsch ausgeführt werden.

Zu einem Programm gehören normalerweise eine Eingabe, eine Verarbeitung und eine Ausgabe:

![Eingabe - Verarbeitung - Ausgabe](IPO.png)

In diesem Abschnitt wirst Du Dein erstes Python-Programm schreiben.


### Aufgabe 1

Öffne einen Texteditor (also *keine IPython-Konsole*) und erstelle eine leere Datei. Schreibe hinein: 

    print("Hannah")
    print(23073)

Speichere die Datei anschließend unter dem Namen `ausgabe.py` ab.

### Aufgabe 2

Nun kannst Du das Programm ausführen.

* Unter **Anaconda** drückst Du dazu den *"Play"*-Knopf oder `F5`.
* Mit einer **Kommandozeile** wechselst Du in das Verzeichnis mit der Datei `ausgabe.py` und schreibst:

    python3 ausgabe.py


### Aufgabe 3

Erkläre das folgende Programm:

    name = "Emily"
    jahr = 2000
    print(name, jahr)


### Aufgabe 4

Was tut die `print`-Anweisung? Wir versuchen sie einmal wegzulassen.
Schreibe in ein **Programm** (eine Datei mit der Endung `.py`):

    name = "Emily"
    name

Was siehst Du, wenn Du das Programm ausführst?

### Aufgabe 5

Erkläre die folgende Anweisung:

    print("Emily\tSmith\n2000")

### Aufgabe 6

Manche Babys haben berühmte Namensvettern. Schreibe ein Programm, welches folgende Ausgabe produziert:

    Harry      Hermione      Severus
    Tyrion     Daenerys      Frodo
    Luke       Leia          Darth

Erschwere Dir die Aufgabe, indem Du:

* die Ausgabe mit einem einzigen `print`-Befehl erzeugst.
* die Namen vorher in Variablen speicherst.

# Eingabe von der Tastatur

Nun werden wir die Tastatur als Eingabemedium an unser Programm anschließen.

### Aufgabe 1

Was tut das folgende Programm?

    name = input("Wie heißt Du? ")
    print(name)


### Aufgabe 2

Welche `input`-Befehle sind korrekt?

<quiz name="">
    <question multiple>
        <p>Markiere alle korrekten Aussagen:</p>
        <answer correct><code>a = input()</code></answer>
        <answer correct><code>a = input("gib eine Zahl ein.")</code></answer>
        <answer><code>a = input(gib Deinen Namen ein)</code></answer>
        <answer correct><code>a = input(3)</code></answer>
        <explanation>Die Funktion <code>input()</code> akzeptiert unterschiedliche Argumente, die alle ausgegeben werden. Text (Strings) muss jedoch in Anführungszeichen eingeschlossen sein.</explanation>
    </question>
</quiz>


### Aufgabe 3

Schreibe ein Programm, das nach einem Namen und einer Zahl fragt, und beides in einem Satz ausgibt, z.B.:

    Bobby ist 3 Jahre alt.


### Aufgabe 7

<quiz name="">
    <question multiple>
<p>Welche <code>print</code>-Anweisungen sind korrekt?</p>

<answer correct><code>print("9" + "9")</code></answer>
<answer><code>print "neun"</code></answer>
<answer correct><code>print(str(9) + "neun")</code></answer>
<answer correct><code>print(9 + 9)</code></answer>
<answer correct><code>print(neun)</code></answer>
<explanation>Die <code>print</code>-Funktion wandelt alles in Strings um. <code>print(neun)</code> ist syntaktisch korrekt, es muss aber eine Variable mit den Namen <code>neun</code> existieren.</explanation>
</question>
</quiz>
