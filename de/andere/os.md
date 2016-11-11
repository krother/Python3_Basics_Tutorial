
# Verzeichnisse durchsuchen

Bei manchen Datensätzen sind nicht alle Namen der benötigten Dateien im Voraus bekannt. Das Programm muß sich die Namen dann selbst zusammensuchen. Glücklicherweise bietet Python auch hierfür eine schlagfertige Lösung: Das Standardmodul `'os'`.

### Aufgabe 1

Fülle die Lücken im Text.

![os exercise](../exercises/os.png)

### Aufgabe 2

Erkläre den folgenden Code:

    import os
    for dirname in os.listdir('.'):
        print(dirname)


### Aufgabe 3

Schreibe ein Programm, welches die Dateien im Ordner mit den Babynamen auszählt. Gib diese Anzahl aus.

Verifiziere von Hand (mit dem Explorer), daß die Zahl korrekt ist. 

