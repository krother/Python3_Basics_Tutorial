pandas Cheat Sheet
==================

Einstieg
--------

pandas importieren
~~~~~~~~~~~~~~~~~~

::

    import pandas as pd

Series erstellen
~~~~~~~~~~~~~~~~

::

    s = pd.Series([1, 2, 3], index=['A', 'B', 'C'], name='col1')

DataFrame erstellen
~~~~~~~~~~~~~~~~~~~

::

    data = [[1, 4], [2, 5], [3, 6]]
    index = ['A', 'B', 'C']
    df = pd.DataFrame(data, index=index, columns=['col1', 'col2'])

DataFrame laden
~~~~~~~~~~~~~~~

::

    df = pd.read_csv('dateiname.csv', 
         sep=',', 
         names=['col1', 'col2'], 
         index_col=0, 
         encoding='utf-8',
         nrows=3)

Zeilen und Spalten indizieren
-----------------------------

eine Spalte auswählen
~~~~~~~~~~~~~~~~~~~~~

::

    df['col1']

mehrere Spalten auswählen
~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df[['col1', 'col2']]

erste n Zeilen anzeigen
~~~~~~~~~~~~~~~~~~~~~~~

::

    df.head(2)

letzte n Zeilen anzeigen
~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.tail(2)

Zeilen nach Index-Werten auswählen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.ix['A']
    df.ix[['A', 'B']]

Zeilen nach Position auswählen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.ix[1]
    df.ix[1:]

Datenaufbereitung
-----------------

nach Werten filtern
~~~~~~~~~~~~~~~~~~~

::

    df[df['col1'] > 1]

nach Spalten sortieren
~~~~~~~~~~~~~~~~~~~~~~

::

    df.sort(['col2', 'col2'], ascending=[False, True])

doppelte Zeilen identifizieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.duplicated()

eindeutige Zeilen finden
~~~~~~~~~~~~~~~~~~~~~~~~

::

    df['col1'].unique()

Spalten und Zeilen vertauschen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df = df.transpose()

eine Spalte löschen
~~~~~~~~~~~~~~~~~~~

::

    del df['col2']

ganzes DataFrame kopieren
~~~~~~~~~~~~~~~~~~~~~~~~~

::

    kopie = df.copy()

Mehrere DataFrames vertikal verketten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df2 = df + 10
    pd.concat([df, df2])

DataFrames horizontal verbinden
-------------------------------

::

    df3 = pd.DataFrame([[1, 7], [8, 9]], 
              index=['B', 'D'], 
              columns=['col1', 'col3'])

nur komplett definierte Zeilen (INNER JOIN)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.merge(df3)

linke Spalte bleibt vollständig (LEFT OUTER JOIN)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.merge(df3, how='left')

rechte Spalte bleibt vollständig (RIGHT OUTER JOIN)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.merge(df3, how='right')

alle Einträge vollständig (OUTER JOIN)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.merge(df3, how='outer')

Zeilen über Indices zusammenführen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.merge(df3, left_index=True, right_index=True

unbesetzte Werte auffüllen oder löschen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.fillna(0.0)
    df.dropna()

eigene Funktion anwenden
~~~~~~~~~~~~~~~~~~~~~~~~

::

    def func(x): return 2**x
    df.apply(func)

Arithmetik und Statistik
------------------------

Addition zu allen Werten
~~~~~~~~~~~~~~~~~~~~~~~~

::

    df + 10

Summe über Spalten
~~~~~~~~~~~~~~~~~~

::

    df.sum()

kumulative Summe über Spalten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.cumsum()

Mittelwert über Spalten
~~~~~~~~~~~~~~~~~~~~~~~

::

    df.mean()

Standardabweichung über Spalten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.std()

Häufigkeit aller Werte ausgeben
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df['col1'].value_counts()

Deskriptive Statistiken für Spalten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.describe()

hierarchische Indizierung
-------------------------

hierarchischen Index erstellen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.stack()

hierarchischen Index auflösen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.unstack()

Aggregation
-----------

Gruppen bilden
~~~~~~~~~~~~~~

::

    g = df.groupby('col1')

über Gruppen iterieren
~~~~~~~~~~~~~~~~~~~~~~

::

    for i, group in g:
        print(i, group)

Gruppen aggregieren
~~~~~~~~~~~~~~~~~~~

::

    g.sum()
    g.prod()
    g.mean()
    g.std()
    g.describe()

Spalten aus Gruppen auswählen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    g['col2'].sum()
    g[['col2', 'col3']].sum()

eigene Funktion auf jede Gruppe anwenden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    def strsum(group):
        return ''.join([str(x) for x in group.values])
    g['col2'].apply(strsum)

Datenexport
-----------

Daten als NumPy-Array
~~~~~~~~~~~~~~~~~~~~~

::

    df.values

Daten als CSV-Datei speichern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.to_csv('ausgabe.csv', sep=",")

DataFrame als Tabellen-String formatieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.to_string()

DataFrame zu Dictionary konvertieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.to_dict()

Visualisierung
--------------

::

    import pylab as plt
    plt.figure()

Streudiagramm
~~~~~~~~~~~~~

::

    df.plot.scatter('col1', 'col2', style='ro')

Balkendiagramm
~~~~~~~~~~~~~~

::

    df.plot.bar(x='col1', y='col2', width=0.7)

Flächendiagramm
~~~~~~~~~~~~~~~

::

    df.plot.area(stacked=True, alpha=1.0)

Box-and-Whisker-Plot
~~~~~~~~~~~~~~~~~~~~

::

    df.plot.box()

Histogramm über eine Spalte
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df['col1'].plot.hist(bins=3)

Histogramm über alle Spalten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    df.plot.hist(bins=3, alpha=0.5)

zuletzt generiertes Diagramm speichern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    plt.savefig('pop.png')

