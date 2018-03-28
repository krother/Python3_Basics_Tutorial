
from collections import Counter

DATEINAME = "alaeddin.txt"
GESUCHT = ['Alaeddin', 'ist', 'hat', 'Djinn', 'Oheim', 'Geist', 'Gold', 'Lampe']

SONDERZEICHEN = ",.()[]@/=+-*;:<>\\?«"

f = open(DATEINAME, encoding='utf-8')
text = f.read()  # ein riesiger String

for s in SONDERZEICHEN:
    text = text.replace(s, ' ')

d = Counter(text.split())

for wort in GESUCHT:
    print(wort, d.get(wort, 0))

print(d.most_common(100))