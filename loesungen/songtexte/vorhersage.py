
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import model_selection

from songs_einlesen import songtexte_auslesen

X = []
y = []
interpreten = ['cash', 'madonna']

for i in interpreten:
    texte = songtexte_auslesen(i + '/')
    X += texte
    y += [i] * len(texte)

ANTEIL_TESTDATEN = 0.2
Xtrain, Xtest, ytrain, ytest = model_selection.train_test_split(X, y, \
                               test_size=ANTEIL_TESTDATEN, \
                               random_state=42)

model = Pipeline([
    ('vectorizer', CountVectorizer(stop_words='english', min_df=3, ngram_range=(1, 1))),
    ('tfidf_transformer', TfidfTransformer()),
    ('bayes_model', MultinomialNB(alpha=0.01)),
])
model.fit(Xtrain, ytrain)

print(model.score(Xtrain, ytrain))
print(model.score(Xtest, ytest))

print(model.predict(["she loves you yeah yeah yeah",
                     "live is a mystery",
                     "an old cowboy rode out one cold and windy day"]))

print(model_selection.cross_val_score(model, X, y, cv=5, 
                                      scoring='accuracy'))

