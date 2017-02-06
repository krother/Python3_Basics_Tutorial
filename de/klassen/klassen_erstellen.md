
### Aufgabe 1

Führe das Codebeispiel `account.py` aus. Erkläre das Programm. 

### Aufgabe 2

Welche Eigenschaften und Methoden hat die Klasse im Beispiel?

### Aufgabe 3

Was ist `self`?

### Aufgabe 4

Erstelle eine abgleitete Klasse ähnlich dem Beispiel `savings_account.py` für ein Girokonto mit Dispositionskredit. Der neue Kontotyp soll eine Dispo-Limit haben. Eine Abhebung soll nur möglich sein, falls das Limit nicht überschritten ist.

### Aufgabe 5

Schreibe eine neue Klasse `Bank`, die eine Liste von Konten enthält. Folgendes soll mit der Bank-Klasse möglich sein:

    bank = Bank()

    bank.konto_anlegen('Max Mustermann')
    bank.konto_anlegen('Frieda Listig')

    for konto in bank.konten:
        print(konto.name)

    print(bank.geld_gesamt())