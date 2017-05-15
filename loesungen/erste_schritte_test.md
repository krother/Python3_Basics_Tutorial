
# Erste Schritte

## Lösungen - Selbsttest

### Leicht

Es gilt, Punkt- vor Strichrechnung zu beachten:

    In [1]: code = 684
    In [2]: (code * 10 - 1) / 7
    Out[2]: 977

Ebenfalls möglich ist, das Zwischenergebnis zu speichern:

    In [2]: z = code * 10 - 1
    In [3]: z / 7


### Mittel

    In [2]: name = "Walter White"
    In [3]: initialien = name[0] + name[7]

### Schwer

Wegen des `'` scheidet dieses Zeichen als Anführungszeichen aus.
Möchte man auch den Zeilenumbruch unterbringen, braucht man ein `\n` oder
dreifache Anführungszeichen.:

    text = "Im Jahr 2014 wurden in den USA\n977 Babys mit dem Namen 'Walter' geboren."

oder

    text = """Im Jahr 2014 wurden in den USA
    977 Babys mit dem Namen 'Walter' geboren."""

