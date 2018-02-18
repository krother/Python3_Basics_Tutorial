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

#
# Vorbereitungen
#

# Anteil Einträge zum Testen, Rest zum Trainieren
ANTEIL_TESTDATEN = 0.2

eminem = songtexte_einlesen("eminem/")
madonna = songtexte_einlesen("madonna/")

print("Madonna: {} songs".format(len(madonna)))
print("Eminem : {} songs".format(len(eminem)))

X = madonna + eminem
y = ['madonna'] * len(madonna) + ['eminem'] * len(eminem)


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
print("\nAnzahl vektorisierter Wörter: {}".format(nwoerter))

# Auswertung des Modells
# wir berechnen, mit welcher Wahrscheinlichkeit
# ein Lied dem richtigen Künstler zugeordnet werden kann
print("\nGenauigkeit auf den Trainingsdaten: ", model.score(Xtrain, ytrain))
print("Genauigkeit auf den Testdaten: ", model.score(Xtest, ytest))


# 10-fache Kreuzvalidierung
# (10x neu gewürfelter Testdatensatz)
# !! Training/Test Split ist bei 0.2 statt 0.8
#
print("\nKreuzvalidierung:")
print(model_selection.cross_val_score(model, X, y, cv=10, scoring='accuracy'))


# besonders diskriminative Wörter ausgeben:
names = np.array(model.named_steps['vectorizer'].get_feature_names())
coef = model.named_steps['bayes_model'].coef_
coef = coef.reshape((len(names),))

# Top-Wörter für Madonna
indices = (-coef).argsort()[:20].tolist()
print("\nCharakteristische Wörter für Madonna:")
print(names[indices])

# Top-Wörter für Eminem
indices = (coef).argsort()[:20].tolist()
print("\nCharakteristische Wörter für Eminem:")
print(names[indices])


#
# Beispiel-Vorhersagen
#
beispiele = [
    "we will dance and have a good time", 
    "my homies are nuts and listen to dumb records",
    "like a dsfjklweh"
]

vorhersagen = model.predict(beispiele)

for satz, vorh in zip(beispiele, vorhersagen):
    print("\nDer Satz '{}' ist vermutlich von '{}'".format(satz, vorh))
