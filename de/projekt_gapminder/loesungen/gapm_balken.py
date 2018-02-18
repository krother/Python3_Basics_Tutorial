
import pandas as pd
import pylab as plt

df = pd.read_csv('../../daten/gapminder_total_fertility.csv', index_col=0)

df = df[['1950', '1975', '2000']]
df = df.ix[['Germany', 'India', 'Bulgaria', 'Chile']]

df.plot.bar(figsize=(5,7))
plt.savefig('balken.png')

df.plot.bar(y='1950', width=0.7, color='orange', figsize=(5,7))
plt.savefig('balken2.png')

