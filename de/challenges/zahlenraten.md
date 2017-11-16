
## Zahlenraten

Schreibe ein Programm, das eine Zufallszahl zwischen 1 und 100 auswürfelt:

    import random

    zahl = random.randint(1, 100)

Der Spieles soll diese Zahl raten. Das Programm gibt Hinweise, ob die geratene Zahl zu groß, zu klein oder ein Treffer ist. Der Spieler kann so oft raten, bis die richtige Zahl getroffen wurde.

### Beispielausgabe:

    Ich habe mir eine Zahl ausgedacht.
    Rate die Zahl.

    Bitte gib eine Zahl ein (1-100): 33
    Die Zahl ist zu gross.

    Bitte gib eine Zahl ein (1-100): 22
    Die Zahl ist zu gross.

    Bitte gib eine Zahl ein (1-100): 11
    Die Zahl ist zu klein.

    Bitte gib eine Zahl ein (1-100): 17
    Die Zahl ist zu gross.

    Bitte gib eine Zahl ein (1-100): 14
    Die Zahl ist zu gross.

    Bitte gib eine Zahl ein (1-100): 12
    Die Zahl ist zu klein.

    Bitte gib eine Zahl ein (1-100): 13
    Treffer!
