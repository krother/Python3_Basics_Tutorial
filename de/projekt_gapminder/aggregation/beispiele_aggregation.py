
from beispiele_gruppen import g1, g2, g3, g4, g5, g6

# Aggregation mit Standardfunktionen
gx.mean()
gx.max()
gx.min()
gx.sum()
gx.count()
gx.std()
gx.median()
gx.quantile(0.9)
gx.describe()

# Aggregation mit Spaltenauswahl
gx['population'].describe()

# Aggregation mit Liste von Funktionen
gx.agg(['count', 'mean', 'std'])
gx.agg([('Summe', 'sum')])

# Eigene Aggregatfunktion definieren
def summe_groesser200(array):
    return sum([x for x in array if x>200])

gx.agg(summe_groesser200)

# Eigene Aggregatfunktion mit Parameter
def summe_groesser(array, threshold):
    return sum([x for x in array if x>threshold])

gx.agg(summe_groesser, threshold=200)

# Iterieren über Gruppen
for name, group in gx:
    print(name)
    print(group)

# Gruppen als Dictionary
dict(list(gx))

# Transformation mit Funktionsname
gx.transform('mean')

# Transformation mit Funktion
gx.transform(len)

# Transformation mit eigener Funktion
def normalisieren(array):
    return array - array.mean()

gx.transform(normalisieren)

# Beliebige Funktion anwenden
def erste_zwei(df):
    return df.head(2)

gx.apply(erste_zwei)
