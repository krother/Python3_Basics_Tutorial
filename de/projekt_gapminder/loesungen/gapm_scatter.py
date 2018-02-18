
import pandas as pd
import pylab as plt

fer = pd.read_csv('../../daten/gapminder_total_fertility.csv', index_col=0)
lex = pd.read_excel('../../daten/gapminder_lifeexpectancy.xlsx', index_col=0)

print(fer.shape)
print(lex.shape)

df = lex.merge(fer, left_index=True, right_index=True)

print(df.columns)

df = df[[2015, '2015']]

df = df.dropna()

df.plot.scatter(2015, '2015', style='ro')
plt.savefig('korrelation.png')
