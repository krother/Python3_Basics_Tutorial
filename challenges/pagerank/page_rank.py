"""
PageRank algorithm

https://en.wikipedia.org/wiki/PageRank
"""

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


pairs1 = pd.read_csv('cities.csv', names=['city1', 'city2'])
pairs2 = pd.read_csv('cities.csv', names=['city2', 'city1'])
pairs = pd.concat([pairs1, pairs2])

# create adjacency matrix
adjacency = pd.crosstab(pairs['city1'], pairs['city2'])
print(adjacency.values)

# run PageRank algorithm with NetworkX library
g = nx.from_pandas_adjacency(adjacency)

rank = nx.pagerank(g, alpha=0.85)

connections = adjacency.sum(axis=1)
rank = pd.Series(rank)

df = pd.DataFrame({'connections': connections, 'rank': rank})
df = df.sort_values(by='rank', ascending=False)
print(df.head(10))


# color by rank
plt.figure()
colors = [df.loc[city]['rank'] for city in g.nodes()]
nx.draw(g, node_color=colors, labels=dict(zip(g.nodes(), g.nodes())))

plt.show()
