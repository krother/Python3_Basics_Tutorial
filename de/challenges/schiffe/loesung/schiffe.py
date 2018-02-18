
import pandas as pd
import pylab as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


# Aufgabe 1
#
# Lies die Datei mit den größten Schiffen der Welt ein
# Setze den Index auf die Schiffsnamen.
df = pd.read_csv('schiffe.csv', index_col=0)

# Welches Schiff hat einen Tiefgang unter 3 Metern? (vorletzter Buchstabe)
print(df[df['Tiefgg'] < 3.0].transpose())


# Aufgabe 2
#
# Verschaffe Dir einen Überblick
# über die Werte der Spalten *Art* und *Status*.
print("\nArten von Schiffen:")
print(df['Art'].value_counts())
print("\nStatus von Schiffen:")
print(df['Status'].value_counts())


# Aufgabe 3
#
# Schaue nach möglichen Korrelationen.
pd.scatter_matrix(df)
plt.savefig('matrix.png')


# Aufgabe 4
#
# Plotte Länge gegen Höhe als Streudiagramm.
df.plot.scatter('Länge', 'Höhe')
plt.savefig('scatter.png')


# Aufgabe 5
#
# Einer der Einträge enthält einen **Datenfehler**.
print("\nEintrag mit Datenfehler:")
print(df.ix['HMS Hood'].transpose())


# Aufgabe 6
#
# Extrahiere einige Spalten
# Lösche die Einträge mit `NaN`-Werten
subset = df[['BRZ', 'DWT', 'Länge', 'Breite', 'Tiefgg']]
subset = subset.dropna()

# Aufgabe 7
#
# Extrahiere die Daten als NumPy-Array
X = subset.values


# Aufgabe 9
#
# Skaliere die Daten auf Werte zwischen 0 und 1.
scaler = MinMaxScaler()
scaler.fit(X)
X = scaler.transform(X)


# Aufgabe 8
#
# Clustere die Daten nach der **KMeans**-Methode in 4 Cluster
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)
print("\nClusterzuordnungen der {} Schiffe:".format(X.shape[0]))
print(kmeans.labels_)


# Speichere die Cluster als zusätzliche Spalte
clusterspalte = pd.Series(kmeans.labels_, index=subset.index)
subset['cluster'] = clusterspalte


# Aufgabe 10
#
# Färbe die Cluster ein
def farbe_zuweisen(clusternr):
    FARBEN = ['blue', 'green', 'red', 'orange']
    return FARBEN[clusternr]


colors = subset['cluster'].apply(farbe_zuweisen)
subset.plot.scatter('Länge', 'Breite', subset['Länge'] / 10, c=colors)
plt.savefig('clusters.png')


# Aufgabe 11
#
# Hauptkomponentenzerlegung
pca = PCA(n_components=2)
pca.fit(X)
xpca = pca.transform(X)

plt.figure()
plt.plot(xpca[:, 0], xpca[:, 1], 'ro')
plt.xlabel('1. Hauptkomponente ("Größe")')
plt.xlabel('2. Hauptkomponente ("Länglichkeit")')
plt.savefig('pca.png')
# Hier haben wir Glück, daß sich die Hauptkomponenten mit Wörtern wie Größe
# beschreiben lassen. Meist ist das nicht so.


# Aufgabe 12
#
# Koeffizienten der Hauptkomponenten
# ausgeben und plotten
print("\nKoeffizienten der Hauptkomponenten")
print(pca.components_)
names = list(subset.columns)

plt.figure()
plt.matshow(pca.components_, cmap='viridis')
plt.yticks([0, 1], ["1. Hauptkomponente", "2. Hauptkomponente"])
plt.colorbar()
plt.xticks(range(len(names)), names, rotation=60, ha='left')
plt.xlabel('Eigenschaft')
plt.ylabel('Hauptkomponente')
plt.savefig('PCA_heatmap.png')
