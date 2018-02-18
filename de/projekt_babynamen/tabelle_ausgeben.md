
# Dateien schreiben

### Aufgabe 1

Bilde Paare aus Python-Anweisungen und deren Bedeutungen.

![file exercise](../exercises/files.png)


### Aufgabe 2

Führe das folende Programm aus. Erkläre was passiert.

    namen = ['Adam', 'Bob', 'Charlie']

    f = open('jungs.txt', 'w')
    for name in namen:
        f.write(name + '\n')
    f.close()


### Aufgabe 3

Lösche das `+ '\n'` aus dem Programm und führe es noch einmal aus. Was passiert?


### Aufgabe 4

Ergänze die folgenden Anweisungen durch `int()` oder `str()`, so daß sie alle funktionieren.

     In [1]: 9 + 9

     In [2]: 9 + '9'

     In [3]: '9' + '9'

     In [4]: 9 * '9'


### Aufgabe 5

Schreibe ein Programm, welches die folgenden Daten in eine zweispaltige Textdatei schreibt.

    namen = ["Emma", "Olivia", "Sophia", "Isabella", 
             "Ava", "Mia", "Emily"]
    anzahlen = [20799, 19674, 18490, 16950, 
               15586, 13442, 12562]
