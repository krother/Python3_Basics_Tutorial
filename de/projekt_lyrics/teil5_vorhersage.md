
# Teil 5: Vorhersage

Hier werden wir ein Standard-Kochrezept nachbauen (siehe [http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html](http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)).

## Aufgabe 5.1

Erstelle ein neues Modul `vorhersage.py`.

Importiere die Funktion zum Einlesen aus dem Modul `songs_einlesen.py` ein:

    from songs_einlesen import songtexte_auslesen

## Aufgabe 5.2

Bereite die Daten zur Vorhersage vor, indem Du in `X` die Liste mit Songtexten sammelst, in `y` die Namen der Interpreten. Zum Beispiel:

    X = madonna + eminem
    y = ['madonna'] * len(madonna) + ['eminem'] * len(eminem)

Stelle sicher, daß X und y gleich lang sind.

## Aufgabe 5.3

Importiere ein paar Sachen aus `scikit-learn`:

    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.pipeline import Pipeline
    from sklearn import model_selection

## Aufgabe 5.4

Zerlege den Datensatz in Trainings- und Testdaten. Setze für `ANTEIL_TESTDATEN` eine Zahl zwischen 0 und 1 ein:

Xtrain, Xtest, ytrain, ytest = \
    model_selection.train_test_split(X, y, test_size=ANTEIL_TESTDATEN)

## Aufgabe 5.5

Baue das Modell:

    model = Pipeline([
        ('vectorizer', CountVectorizer(min_df=3, ngram_range=(1, 1))),
        ('tfidf_transformer', TfidfTransformer()),
        ('bayes_model', MultinomialNB(alpha=1.0)),
    ])
    model.fit(Xtrain, ytrain)

## Aufgabe 5.6

Gib die Anzahl vektorisierter Wörter aus:

    vect = model.named_steps['vectorizer']
    print(len(vect.vocabulary_))

## Aufgabe 5.7

Werte das Modell aus:

    print("Genauigkeit: ", model.score(Xtest, ytest))

Werte das Modell auch für den Testdatensatz aus. Wie bewertest Du das Ergebnis?

## Aufgabe 5.8

Verändere den Parameter `alpha`. Wie verändert sich die Vorhersage?

## Aufgabe 5.9

Führe eine 10-fache Kreuzvalidierung durch:

    print(model_selection.cross_val_score(model, X, y, 
    cv=10, scoring='accuracy'))


## Aufgabe 5.10

Führe eine Vorhersage durch:

    model.predict(["take the 8mile road in detroit"])

## Aufgabe 5.11

Gib typische Wörter für die verglichenen Künstler aus:

    import numpy as np
    names = np.array(model.named_steps['vectorizer'].get_feature_names())

    coef = model.named_steps['bayes_model'].coef_
    coef = coef.reshape((len(names),))

    # Top-Wörter für 1. Interpreten
    indices = (-coef).argsort()[:20].tolist()
    print(names[indices])

    # Top-Wörter für 2. Interpreten
    indices = (coef).argsort()[:20].tolist()
    print(names[indices])

## Aufgabe 5.11

Probiere unterschiedliche Optionen aus:

* variiere den Anteil der Testdaten
* variiere `min_df` beim `CountVectorizer`
* gib beim `CountVectorizer` die Option `stop_words='english'`
* variiere `ngram_range` beim `CountVectorizer`
