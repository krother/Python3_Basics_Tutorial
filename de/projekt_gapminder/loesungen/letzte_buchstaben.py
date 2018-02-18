
import pandas as pd

names = []
PATH = 'names'

for year in range(1880, 2015):
    fn = '{}/yob{}.txt'.format(PATH, year)    
    data_frame = pd.read_csv(fn, names=['name', 'gender', 'count'])
    data_frame['year'] = year
    names.append(data_frame)

names = pd.concat(names)

names['last'] = names['name'].apply(lambda x:x[-1])

df = names.groupby(['gender', 'last', 'year'])['count'].sum()

df = df.unstack()
df = df.ix['M']
df = df / df.sum()

df[[1910, 2010]].plot.bar()
plt.savefig('/home/krother/Desktop/barsM.png')

df = df.transpose()

df[['d', 'n', 'y']].plot()
plt.savefig('/home/krother/Desktop/timelineM.png')

