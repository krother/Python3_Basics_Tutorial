import pandas as pd
import numpy as np

df = pd.read_csv('grosse_laender_2015.csv', index_col=0)

df['population'] = df['population'] / 1000000)
df['population'] = df['population'].apply(round)

# 1. nach einer Spalte
g1 = df.groupby('continent')

# 2. nach einem Array gleicher Länge
industrialized = np.array([False, True, True, True, False, True, True, False, False, False, True, True])
g2 = df.groupby(industrialized)

# 3. nach einem Dictionary mit Schlüsseln auf den Index
language = {'Bangladesh':'HD', 'Brazil':'PT', 'China':'CN', 'India':'HD', 'Indonesia':'ID', 'Japan':'JP', 'Mexico':'ES', 'Nigeria':'NG', 'Pakistan':'AR', 'Philippines':'PP', 'Russia':'RU', 'United States':'EN'}
g3 = df.groupby(language)

# 4. mit einer Funktion
g4 = df.groupby(len)

# 5. mit einer Liste der obigen
g5 = df.groupby(['continent', language, len])

# 6. entlang der X-Achse gruppieren
g6 = df[['population', 'fertility']].transpose().groupby(len, axis=1)
