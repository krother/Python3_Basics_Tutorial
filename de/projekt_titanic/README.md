
# Wer überlebt auf der Titanic

## Ziel

Wir möchten anhand der Angaben über einen Passagier auf der Titanic vorhersagen ob dieser das Unglück überlebt oder nicht.

----

## Aufgaben


### 1. Hypothesen

Sammelt Ideen, was für *Merkmale von Passagieren* die Überlebenschancen auf der Titanic steigern und welche nicht, bevor Ihr das Modell baut.

----

### 2. Vorbereitung

Importiere:

    import pandas as pd
    import pylab as plt
    import numpy as np

### 3. Daten laden

Verwende `pandas`, um die Datei `train.csv` zu laden.

Du findest eine Dokumentation der Daten auf [www.kaggle.com/c/titanic](https://www.kaggle.com/c/titanic).

----

### 4. Histogramm

Erstelle ein Histogramm nach dem Alter nach Überleben gruppiert:

    df.groupby('Survived')['Age'].hist(alpha=0.5)

----

### 5. Balkendiagramm

Erstelle ein Balkendiagramm mit den Häufigkeiten gruppiert nach Passagierklasse nach Überleben:

    g = df.groupby(['Survived', 'Pclass'])
    g = g['Name'].count()
    g = g.unstack()
    g.plot().bar()

**Wozu dient der Befehl `unstack`?**

----

### 6. Noch ein Balkendiagramm

Gruppiere als drittes Kriterium zusätzlich nach Geschlecht.

----

### 7. Paarplot

Jetzt plotten wir alles gegen alles!

    pd.scatter_matrix(df, figsize=(15,15))

**Anmerkung:** Da die meisten der Daten *kategorisch* sind, kann man im Diagramm nicht so viel sehen. Die Darstellung ist aber oft so praktisch, daß ich sie Euch nicht vorenthalten wollte.


### 7.1 Einfärben

Färbe die Überlebenden blau ein und die Ertrunkenen rot. Schreibe dazu eine Funktion `make_col(x)`, die je nach x einen anderen Farbcode `(R, G, B)` zurück liefert.

Damit können wir eine Spalte mit Farbangaben erstellen:

    col = df['Survived'].apply(make_color)

Und diese als zusätzlichen Parameter `c=col` in der Funktion `scatter_matrix` angeben.


### 7.2 Auswählen von Spalten

Wähle alle Spalten außer `"Survived"` für den Paarplot aus.


----

### 8. Datenaufbereitung

* Lösche die Spalten `"Name"` und `"Cabin"` aus dem Datensatz.
* Lösche alle Zeilen mit Lücken mit `dropna()`
* Speichere die Spalten `"Pclass"` und `"Age"` in einem DataFrame `X`.
* Speichere die Spalte `"Survived"` in einer Variable `y`.

Wandle beide DataFrames in NumPy Arrays um:

    X = X.values
    y = y.values

----

### 9. Ein Modell erstellen

Teile den Datensatz in Trainings- und Testdaten auf:

    from sklearn.model_selection import train_test_split

    Xtrain, ytrain, Xtest, ytest = train_test_split(X, y, random_state=0)

Nun erstellen wir eines der einfachsten möglichen maschinellen Lernmodelle nach dem k-nächste-Nachbarn-Verfahren:

    from sklearn.neighbors import KNeighborsClassifier

    m = KNeighborsClassifier(n_neighbors=1)

und trainieren das Modell mit unseren Trainingsdaten:

    m.fit(Xtrain, ytrain)

----

### 10. Das Modell auswerten

Berechne die Genauigkeit des Modells für die Trainingsdaten:

    print(m.score(Xtrain, ytrain))


Berechne die Genauigkeit auch für die Testdaten. Vergleiche die Zahlen und erkläre die Unterschiede.

#### Frage

Ist dies ein gutes Modell?

----

### 11. Vorhersage

Erstelle Datensätze für weitere Passagiere:

    import numpy as np

    leo = np.array([[22, 3]])
    kate = np.array([[25, 1]])

und erstelle eine Vorhersage für diese:

    print(m.predict(leo))
    print(m.predict(kate))

----

### 12. Mehr Daten!!!

Wiederhole den Modellbau, indem Du mehr Daten berücksichtigst. Nimm 2-3 zusätzliche Spalten auf. Verbessert sich an der Qualität der Vorhersage etwas?

#### 11.1 Dummy-Variablen

Um die *kategorischen* Merkmale `"Sex"` oder `"Embarked"` mit aufzunehmen, benötigst Du folgende Funktion:

    pd.get_dummies(df['Sex'])

baue die Dummy-Variablen in Deinen Datensatz ein, bevor Du ihn in Trainings- und Testdaten aufteilst.

Wie verändert sich die Genauigkeit des Modells?

----

### 13. Weitere Modelle

Verschaffe Dir einen Überblick über die Funktionsweise eines der folgenden Modelle zur Klassifikation:

| Modell | Klasse in scikit-learn |
|--------|------------------------|
| logistische Regression | sklearn.linear_model.LogisticRegression |
| Random Forest | sklearn.ensemble.RandomForestClassifier |
| Support Vector Machine | sklearn.svm.SVC |
| neuronale Netze | sklearn.neural_network.MLPClassifier |

Als Quelle dienen Wikipedia und [scikit-learn.org](http://scikit-learn.org)

Wende eines dieser Modelle auf den Datensatz an, indem Du die Klasse 
`KNeighborsClassifier` durch die aus der Tabelle ersetzt. Gib keine Parameter an, sondern verwende die Standardeinstellungen.

Welche Genauigkeit erreicht Ihr?

### 13.1 Koeffizienten bei der logistischen Regression

Schaue Dir die berechneten Koeffizienten von `LogisticRegression` an:

    for lab, coef in zip(labels, m.coef_[0]):
        print("{:10s}\t{:8.3f}".format(lab, coef))

### 13.2 Maximale Tiefe beim Random Forest

Vergleiche die Parameter `max_depth=2`, `max_depth=3` und `max_depth=10`. Wie wirken sich die Einstellungen auf die Vorhersagequalität aus?

### 13.3 Skalieren

Skaliere die Eingabedaten für das neuronale Netzwerk:

    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    scaler.fit(Xtrain)
    Xtrain = scaler.transform(Xtrain)
    Xtest = scaler.transform(Xtest)


### 13.4 Iterationen beim neuronalen Netzwerk

Setze den Parameter `hidden_layer_sizes` auf 100. Was ändert sich?

Erhöhe den Parameter `max_iter`. Was ändert sich?

----

### 14. Zusatzaufgabe: Die Vorhersage einschicken

Sende eine Vorhersage auf [kaggle.com](http://www.kaggle.com) ein und schaue wie erfolgreich Dein Modell ist.
