"""
TEIL 5

Vorhersagen, von wem ein Song ist.

Wir verwenden einen einfachen Bayes-Klassifikator basierend
auf dem "bag of words" Ansatz nach
http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import model_selection
from songs_einlesen import songtexte_einlesen
import numpy as np
import time

#
# Vorbereitungen
#

# Anteil Einträge zum Testen, Rest zum Trainieren
ANTEIL_TESTDATEN = 0.2

eminem = songtexte_einlesen("eminem/")
madonna = songtexte_einlesen("madonna/")
beatles = songtexte_einlesen("beatles/")

print("Madonna: {} songs".format(len(madonna)))
print("Eminem : {} songs".format(len(eminem)))
print("Beatles : {} songs".format(len(beatles)))

X = madonna + eminem + beatles
y = ['Madonna'] * len(madonna) + ['Eminem'] * len(eminem) + ['Beatles'] * len(beatles)


# Datensatz in Trainingsdaten und Testdaten aufteilen
Xtrain, Xtest, ytrain, ytest = \
    model_selection.train_test_split(X, y, test_size=ANTEIL_TESTDATEN, random_state=42)


#
# Vorhersagepipeline
#

# Glättungsparameter für das Vorhersagemodell
# 1.0   - Standardwert wenn alle Wörter informationsträchtig
# < 1.0 - reduziert Glättung wenn viele nonsense-Wörter dabei sind
ALPHA = 0.1

# Wörter müssen mindestens MIN_DF Mal vorkommen
MIN_DF=10

model = Pipeline([
        # Textfeld in Wortvektoren überführen
        ('vectorizer', CountVectorizer(min_df=MIN_DF, ngram_range=(1, 1))),
        # gezählte Wörter in Anteile überführen
        ('tfidf_transformer', TfidfTransformer()),
        # eigentliches Vorhersagemodell
        ('bayes_model', MultinomialNB(alpha=ALPHA)),
])

# Modell trainieren
model.fit(Xtrain, ytrain)

# Anzahl Wörter ausgeben
vect = model.named_steps['vectorizer']
nwoerter = len(vect.vocabulary_)

# Auswertung des Modells
# wir berechnen, mit welcher Wahrscheinlichkeit
# ein Lied dem richtigen Künstler zugeordnet werden kann
print("\nGenauigkeit auf den Trainingsdaten: ", model.score(Xtrain, ytrain))
print("Genauigkeit auf den Testdaten: ", model.score(Xtest, ytest))


#
# Beispiel-Vorhersagen
#
print('\n\n\nIch kenne mich mit den Beatles, Eminem und Madonna aus.\n')

text = ''
while text != 'X':
    text = input('''

Bitte gib einen englischen Satz ein:
''')
    vorhersagen = model.predict([text])
    print("\nDein Satz hört sich nach {} an.".format(vorhersagen[0]))
    time.sleep(5)
