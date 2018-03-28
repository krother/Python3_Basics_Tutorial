"""
Erstelle einen animierten Scatterplot ähnlich dem von Hans Rosling
"""
import pandas as pd
import pylab as plt
import imageio


# Daten einlesen
fert = pd.read_csv('gapminder_total_fertility.csv', index_col=0)
life = pd.read_excel('gapminder_lifeexpectancy.xlsx', index_col=0)
pop = pd.read_excel('gapminder_population.xlsx', index_col=0)
kontinente = pd.read_csv('kontinente_mit_jahr.txt', sep=',', index_col=0)

print(fert.shape, life.shape, pop.shape)

# Spaltennamen in Integer-Zahlen umwandeln
ncol = [int(x) for x in fert.columns]
fert.set_axis(axis=1, labels=ncol)

ncol = [int(x) for x in kontinente.columns]
kontinente.set_axis(axis=1, labels=ncol)

# in langes Format überführen
sfert = fert.stack()
slife = life.stack()
spop = pop.stack()
skont = kontinente.stack()

# neues DataFrame erstellen
d = {'fertility': sfert, 'lifeexp': slife, 
     'population': spop, 'kontinent': skont}
df2 = pd.DataFrame(data=d)

# nicht belegte Zeilen raus
df2 = df2.dropna()

# Serie von Scatterplots erstellen und schreiben
for jahr in range(1960, 2011):
    dd = df2.unstack(0).loc[jahr].unstack(0)
    dd['farbe'] = 'gray'
    dd['farbe'][dd['kontinent'] == 'Asia'] = 'orange'
    dd['farbe'][dd['kontinent'] == 'Africa'] = 'sienna'
    dd['farbe'][dd['kontinent'] == 'Europe'] = 'firebrick'
    dd['farbe'][dd['kontinent'] == 'North America'] = 'peachpuff'
    dd['farbe'][dd['kontinent'] == 'South America'] = 'darkslateblue'
    dd['farbe'][dd['kontinent'] == 'Oceania'] = 'violet'
    
    pop = list(dd['population'] / 1000000)
    dd.plot.scatter(x='lifeexp', y='fertility', s=pop, c=dd['farbe'])
    plt.axis((40.0, 90.0, 0.0, 8.0))
    plt.title('{}'.format(jahr))
    plt.savefig('bilder/d{}.png'.format(jahr))


# Bilder zu animiertem GIF verbinden
images = []

for i in range(1960, 2011):
    filename = 'bilder/d{}.png'.format(i)
    images.append(imageio.imread(filename))

imageio.mimsave('output.gif', images, fps=10)
