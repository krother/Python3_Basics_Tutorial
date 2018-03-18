
# pandas Kurzreferenz

## Einstieg

### pandas importieren

```python
import pandas as pd
```

### Series erstellen

```python
s = pd.Series([1, 2, 3], index=['A', 'B', 'C'], name='col1')
```

### DataFrame erstellen

```python
data = [[1, 4], [2, 5], [3, 6]]
index = ['A', 'B', 'C']
df = pd.DataFrame(data, index=index, columns=['col1', 'col2'])
```

### DataFrame laden

```python
df = pd.read_csv('dateiname.csv', 
     sep=',', 
     names=['col1', 'col2'], 
     index_col=0, 
     encoding='utf-8',
     nrows=3)
```

## Zeilen und Spalten indizieren

### eine Spalte auswählen

```python
df['col1']
```

### mehrere Spalten auswählen

```python
df[['col1', 'col2']]
```
 
### erste n Zeilen anzeigen

```python
df.head(2)
```

### letzte n Zeilen anzeigen

```python
df.tail(2)
```

### Zeilen nach Index-Werten auswählen

```python
df.ix['A']
df.ix[['A', 'B']]
```

### Zeilen nach Position auswählen

```python
df.ix[1]
df.ix[1:]
```

## Datenaufbereitung

### nach Werten filtern

```python
df[df['col1'] > 1]
```

### nach Spalten sortieren

```python
df.sort(['col2', 'col2'], ascending=[False, True])
```

### doppelte Zeilen identifizieren

```python
df.duplicated()
```

### eindeutige Zeilen finden

```python
df['col1'].unique()
```

### Spalten und Zeilen vertauschen

```python
df = df.transpose()
```

### eine Spalte löschen

```python
del df['col2']
```

### ganzes DataFrame kopieren

```python
kopie = df.copy()
```

### Mehrere DataFrames vertikal verketten

```python
df2 = df + 10
pd.concat([df, df2])
```

## DataFrames horizontal verbinden

```python
df3 = pd.DataFrame([[1, 7], [8, 9]], 
	      index=['B', 'D'], 
	      columns=['col1', 'col3'])
```

### nur komplett definierte Zeilen (INNER JOIN)

```python
df.merge(df3)
```

### linke Spalte bleibt vollständig (LEFT OUTER JOIN)

```python
df.merge(df3, how='left')
```

### rechte Spalte bleibt vollständig (RIGHT OUTER JOIN)

```python
df.merge(df3, how='right')
```

### alle Einträge vollständig (OUTER JOIN)

```python
df.merge(df3, how='outer')
```

### Zeilen über Indices zusammenführen

```python
df.merge(df3, left_index=True, right_index=True
```

### unbesetzte Werte auffüllen oder löschen

```python
df.fillna(0.0)
df.dropna()
```

### eigene Funktion anwenden

```python
def func(x): return 2**x
df.apply(func)
```

## Arithmetik und Statistik

### Addition zu allen Werten 

```python
df + 10
```

### Summe über Spalten

```python
df.sum()
```

### kumulative Summe über Spalten

```python
df.cumsum()
```

### Mittelwert über Spalten

```python
df.mean()
```

### Standardabweichung über Spalten

```python
df.std()
```

### Häufigkeit aller Werte ausgeben

```python
df['col1'].value_counts()
```

### Deskriptive Statistiken für Spalten

```python
df.describe()
```

## hierarchische Indizierung

### hierarchischen Index erstellen

```python
df.stack()
```

### hierarchischen Index auflösen

```python
df.unstack()
```

## Aggregation

### Gruppen bilden

```python
g = df.groupby('col1')
```

### über Gruppen iterieren

```python
for i, group in g:
    print(i, group)
```

### Gruppen aggregieren

```python
g.sum()
g.prod()
g.mean()
g.std()
g.describe()
```

### Spalten aus Gruppen auswählen

```python
g['col2'].sum()
g[['col2', 'col3']].sum()
```

### Spalten transformieren

    import math
    g.transform(math.log)

### eigene Listenfunktion auf jede Gruppe anwenden

```python
def strsum(group):
    return ''.join([str(x) for x in group.values])
g['col2'].apply(strsum)
```

## Datenexport

### Daten als NumPy-Array

```python
df.values
```

### Daten als CSV-Datei speichern

```python
df.to_csv('ausgabe.csv', sep=",")
```

### DataFrame als Tabellen-String formatieren

```python
df.to_string()
```

### DataFrame zu Dictionary konvertieren

```python
df.to_dict()
```

### DataFrame als Excel-Tabelle speichern

    df.to_excel('ausgabe.xlsx')

(benötigt Paket `xlwt`)

## Visualisierung

```python
import pylab as plt
plt.figure()
```

### Streudiagramm

```python
df.plot.scatter('col1', 'col2', style='ro')
```

### Balkendiagramm

```python
df.plot.bar(x='col1', y='col2', width=0.7)
```

### Flächendiagramm

```python
df.plot.area(stacked=True, alpha=1.0)
```

### Box-and-Whisker-Plot

```python
df.plot.box()
```

### Histogramm über eine Spalte

```python
df['col1'].plot.hist(bins=3)
```

### Histogramm über alle Spalten

```python
df.plot.hist(bins=3, alpha=0.5)
```

### Achsenmarkierungen einstellen

    labels = ['A', 'B', 'C', 'D']
    positions = [1.0, 2.0, 3.0, 4.0]
    plt.xticks(positions, labels)
    plt.yticks(positions, labels)

### Zu plottenden Bereich wählen
    
    plt.axis([0.0, 2.5, 0.0, 10.0])
    # [x von, x bis, y von, y bis]

### Diagramm und Achsen beschriften

    plt.title('Korrelation')
    plt.xlabel('Nunstück')
    plt.ylabel('Slotermeyer')

### zuletzt generiertes Diagramm speichern

    plt.savefig('plot.png')
    plt.savefig('plot.png', dpi=300)
    plt.savefig('plot.svg')
