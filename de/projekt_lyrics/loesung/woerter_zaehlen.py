"""
BONUS:

Wörter aus den Songs einlesen und zählen.
"""
from collections import Counter
from songs_einlesen import songtexte_einlesen
import re


# Songtexte einlesen
korpus = songtexte_einlesen('direstraits/')
print("Dokumente im Korpus:", len(korpus))

# Korpus als einen String vorbereiten
korpus = ' '.join(korpus)
print("\nZeichen im Korpus:", len(korpus))

# alles in Kleinbuchstaben
korpus = korpus.lower()

# HTML-Tags rauswerfen
korpus = re.sub("\<br\>", "", korpus)

# restliche Sonderzeichen weg
korpus = re.sub('[^\w]', ' ', korpus)

# in Wörter aufteilen
words = korpus.split()

# kurze Wörter rauswerfen
filtered = []
for w in words:
    if len(w) >= 4:
        filtered.append(w)
words = filtered

# Counter ist ein spezielles Dictionary zum Zählen
c = Counter()
c.update(words)

# häufigste 20 Wörter ausgeben
for k in c.most_common(20):
    print("{:20s}{:10d}".format(k[0], c[k[0]]))
