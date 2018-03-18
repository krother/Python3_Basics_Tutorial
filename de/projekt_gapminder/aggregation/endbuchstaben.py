"""
Analyse der Endbuchstaben von Babynamen
mit pandas
"""
import pandas as pd
import pylab as plt

# Aufgabe 1
#
# Lies die Babynamen aller 135 Jahrgänge in ein einzelnes DataFrame ein.
jahrgaenge = []
for jahr in range(1880, 2015):
    dateiname = '../../babynamen/names/yob{}.txt'.format(jahr)
    df = pd.read_csv(dateiname, names=['name', 'geschlecht', 'anzahl'])
    df['jahr'] = jahr
    jahrgaenge.append(df)

df = pd.concat(jahrgaenge)

# Aufgabe 2
#
# Endbuchstabe als neue Spalte einfügen
def endbuchstabe(s):
    """bekommt einen String und gibt den letzten Buchstaben zurück"""
    return s[-1]


ende = df['name'].apply(endbuchstabe)
df['letzter'] = ende


# Aufgabe 3
#
# Summe der Vornamen nach Geschlecht, Anfangsbuchstabe und Jahr gruppiert.
g = df.groupby(['geschlecht', 'letzter', 'jahr'])
gruppiert = g['anzahl'].sum()
print(gruppiert.head())


# Aufgabe 4
#
# Anteil an den gesamten Vornamen eines Jahrgangs
# für Jungen
gruppiert = gruppiert.ix['M']
gruppiert = gruppiert.unstack()
gruppiert = gruppiert / gruppiert.sum()
print(gruppiert.head())


# Aufgabe 5
#
# Zeichne ein Balkendiagramm für die Jahrgänge 1910 und 2010
jahre = gruppiert[[1910, 2010]]
jahre.plot.bar()
plt.xlabel('Endbuchstabe')
plt.ylabel('Anteil')
plt.savefig('barplot.png')


# Aufgabe 6
#
# Zeichne ein Liniendiagramm für die Endbuchstaben d, n und y
# im zeitlichen Verlauf
verlauf = gruppiert.transpose()
verlauf[['d', 'n', 'y']].plot()
plt.xlabel('Jahr')
plt.ylabel('Anteil')
plt.savefig('linien.png')
