
def fakultaet(zahl):
    """Berechnet die Fakultaet der gegebenen Zahl."""
    if zahl > 1:
        return zahl * fakultaet(zahl - 1)
    else:
        return 1

x = int(input('Bitte gib eine Zahl ein: '))
y = fakultaet(x)
print ("Das Ergebnis ist:\n{}! = {}}".format(x, y))
