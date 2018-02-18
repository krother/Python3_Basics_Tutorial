
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
import pylab as plt
import numpy as np

# 1. Daten laden
df = pd.read_csv('train.csv', index_col=0)

# 2. Histogramm
plt.figure()
df.groupby('Survived')['Age'].hist(alpha=0.5)
plt.savefig('agehist.png')

# 3. Balkendiagramm
sv = df.groupby(['Survived', 'Pclass'])['Name'].count()
sv.unstack().plot.bar()
plt.savefig('bars.png')


# 4. Noch ein Balkendiagramm
sv = df.groupby(['Survived', 'Pclass', 'Sex'])['Name'].count()
sv.unstack().plot.bar()
plt.savefig('bars_gruppen.png')


# 5. Paarplot
def make_col(x):
    """Einfärben nach Überleben"""
    if x == 0:
        return (1, 0, 0)  # rot
    else:
        return (0, 0, 1)  # blau


col = df['Survived'].apply(make_col)
pd.scatter_matrix(df, c=col, figsize=(15,15))
plt.savefig('paarplot.png')


# 7. Datenaufbereitung
del df['Cabin']
del df['Name']

df = df.dropna()

X = df[['Pclass', 'Age']].values
y = df['Survived'].values


# 8. Modell erstellen
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=42)

m = KNeighborsClassifier(n_neighbors=1)
m.fit(Xtrain, ytrain)


# 9. Modell auswerten
print("\nk-nächste-Nachbarn:")
print("Genauigkeit auf den Trainingsdaten:", m.score(Xtrain, ytrain))
print("Genauigkeit auf den Testdaten:", m.score(Xtest, ytest))


# 10. Vorhersage
leo = np.array([[22, 3]])   # Jahre, Klasse
kate = np.array([[25, 1]])  # Jahre, Klasse

print("\nVorhersage für Leo:", m.predict(leo))
print("Vorhersage für Kate:", m.predict(kate))


# 11. Mehr Daten
df2 = df[['Pclass', 'Age', 'SibSp', 'Parch']]

dummies = pd.get_dummies(df['Sex'])
df2['female'] = dummies['female']
df2['male'] = dummies['male']

X = df2.values
y = df['Survived'].values

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=42)

m = KNeighborsClassifier(n_neighbors=1)
m.fit(Xtrain, ytrain)

print("\nk-nächste-Nachbarn mit mehr Daten:")
print("Genauigkeit auf den Trainingsdaten:", m.score(Xtrain, ytrain))
print("Genauigkeit auf den Testdaten:", m.score(Xtest, ytest))


# 12. Mehr Modelle

# 12.1 Logistische Regression
m = LogisticRegression()
m.fit(Xtrain, ytrain)

print("\nlogistische Regression:")
print("Genauigkeit auf den Trainingsdaten:", m.score(Xtrain, ytrain))
print("Genauigkeit auf den Testdaten:", m.score(Xtest, ytest))

for lab, coef in zip(df2.columns, m.coef_[0]):
    print("{:10s}\t{:8.3f}".format(lab, coef))


# 12.2 Random Forest
m = RandomForestClassifier(max_depth=3)
m.fit(Xtrain, ytrain)

print("\nRandom Forest:")
print("Genauigkeit auf den Trainingsdaten:", m.score(Xtrain, ytrain))
print("Genauigkeit auf den Testdaten:", m.score(Xtest, ytest))


# 12.3 Support Vector Machine
m = SVC()
m.fit(Xtrain, ytrain)

print("\nSupport Vector Machine:")
print("Genauigkeit auf den Trainingsdaten:", m.score(Xtrain, ytrain))
print("Genauigkeit auf den Testdaten:", m.score(Xtest, ytest))


# 12.3 Skalieren
scaler = MinMaxScaler()
scaler.fit(Xtrain)
Xtrain = scaler.transform(Xtrain)
Xtest = scaler.transform(Xtest)

# 12.4 Neuronales Netzwerk
m = MLPClassifier(hidden_layer_sizes=100, max_iter=1000)
m.fit(Xtrain, ytrain)

print("\nneuronales Netzwerk (Multi-Layer-Perzeptron):")
print("Genauigkeit auf den Trainingsdaten:", m.score(Xtrain, ytrain))
print("Genauigkeit auf den Testdaten:", m.score(Xtest, ytest))
