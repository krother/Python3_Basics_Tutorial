"""
pip install plotly
"""

import pandas as pd
import numpy as np
import plotly as py
import plotly.graph_objs as go

fer = pd.read_csv('../../daten/gapminder_total_fertility.csv', index_col=0)
lex = pd.read_excel('../../daten/gapminder_lifeexpectancy.xlsx', index_col=0)
pop = pd.read_excel('../../daten/gapminder_population.xlsx', index_col=0)

ncol = [int(x) for x in fer.columns]
fer.set_axis(axis=1, labels=ncol)

sfer = fer.stack()
slex = lex.stack()
spop = pop.stack()

df = pd.DataFrame(data={'fertility': sfer, 'lifeexp': slex, 'population': spop})
df = df.dropna()
df = df.stack()
df = df.unstack((1, 2))

# data = [go.Scatter(    # SLOW
data = [go.Scattergl(    # FAST
    x = df[year]['lifeexp'],
    y = df[year]['fertility'],
    mode = 'markers',
    marker = {
        'size': np.sqrt(df[year]['population']) * 0.002,
        'color': 'rgba(64, 64, 192, .9)'
        #'color': np.random.randn(500), #set color equal to a variable
        #'colorscale': 'Viridis',
        },
    text = df.index.tolist()
) for year in range(1960, 2016, 5)]

steps = []
for i, year in enumerate(range(1960, 2016, 5)):
    step = dict(
        method = 'restyle',
        args = ['visible', [False] * len(data)],
    )
    step['args'][1][i] = True # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active = 0,
    currentvalue = {"prefix": "Year: "},
    pad = {"t": 50},
    steps = steps
)]

layout= go.Layout(
    sliders = sliders,
    title= 'Gapminder Data',
    hovermode= 'closest',
    xaxis= dict(
        title= 'life expectancy',
        range=[0, 90],
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'fertility',
        range=[0, 9],
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False
)

plot = py.offline.plot({
    'data': data,
    "layout": layout
    })

# Plot and embed in ipython notebook!
# py.iplot(data, filename='basic-scatter')
