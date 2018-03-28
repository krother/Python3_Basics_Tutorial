"""
Bearbeiten des Babynamen-Projekts mit pandas
"""
import pandas as pd
import pylab as plt

PFAD = 'babynamen/'
babynamen = [] # Liste von DataFrames

for jahr in range(1880, 2017):
    df = pd.read_csv(PFAD + 'yob{}.txt'.format(jahr),
                     names=['name', 'geschlecht', 'anzahl'])
    df['jahr'] = jahr
    babynamen.append(df)

df = pd.concat(babynamen)

jungs = df[df['geschlecht'] == 'M']
maedchen = df[df['geschlecht'] == 'F']    

def initial(s):
    return s[0]

df['erster'] = df['name'].apply(initial)

g = df.groupby(by=['erster', 'jahr'])['anzahl'].sum()
g = g.unstack(0)
g[['M', 'E', 'K', 'W']].plot()
plt.show()
