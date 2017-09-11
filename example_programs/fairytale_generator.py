import random as rr

fchars = ['Hexe',  'Königin', 'Nachtigall', 'Bäuerin', \
         'Prinzessin', 'Ferkel', 'Truhe', \
         'Stiefmutter', 'Fee', 'Ziege', 'Erbse', \
         'Wurst', 'Kerze', 'Maus', 'Katze', 'Birne']

mchars = ['Bär', 'Zwerg', 'Wald', 'Riese', 'König', 'Zauberer', 'Berg', 'Turm', \
         'Prinz', 'Wolf', 'Jäger', 'Bauer', 'Käse', 'Schlüssel', \
         'Köhler', 'Holzfäller', 'Hofnarr', 'Geist', 'Drachen', 'Schwan', \
         'Apfel', 'Kürbis']

plural = ['Bären', 'Zwerge', 'Riesen', 'Könige', 'Zauberer', 'Prinzen', 'Wölfe', \
        'Ferkel', 'Jäger', 'Prinzessinnen', 'Geister', 'Schlüssel', 'Schwäne', \
        'Würste', 'Köhler', 'Holzfäller', 'Hofnarren', 'Drachen', 'Mäuse', 'Katzen', \
        'Hexen', 'Königinnen', 'Nachtigallen', 'Bauern', 'Bäuerinnen', 'Stiefmütter', \
        'Kerzen', 'Drachen', 'Feen', 'Schneider', 'Ziegen', 'Türme', 'Berge', 'Schlösser', \
        'Äpfel']

adj = ['weise', 'dumme', 'tapfere', 'schreckliche', 'edle', 'heldenhafte', 'riesige', 'winzige', \
        'weisse', 'blaue', 'eingebildete', 'rote', 'dunkle', 'schwarze', 'kräftige', 'unsichtbare', \
        'eitle', 'hässliche', 'schöne', 'schlafende', 'verzauberte'
      ]

prep = ['auf', 'unter', 'über', 'an', 'hinter']

primes = [str(p) for p in [2, 3, 5, 7, 9, 13, 99]]

patterns = [
    ("Der %s und der %s", (mchars, mchars)),
    ("Der %s und die %s", (mchars, fchars)),
    ("Die %s und die %s", (fchars, fchars)),
    ("Die %s und der %s", (fchars, mchars)),
    ("Der %s %s dem %s", (mchars, prep, mchars)),
    ("Der %s %s der %s", (mchars, prep, fchars)),
    ("Die %s %s dem %s", (fchars, prep, mchars)),
    ("Die %s %s der %s", (fchars, prep, fchars)),
    ("Der %s %s und die %s", (adj, mchars, plural)),
    ("Die %s %s und die %s", (adj, fchars, plural)),
    ("Die %s %s", (adj, fchars)),
    ("Der %s %s", (adj, mchars)),
    ("Die %s %s", (primes, plural)),
    ]


while 1:
    pattern, var = rr.choice(patterns)
    values = tuple([rr.choice(v) for v in var])
    s = pattern % values
    print(s)
    input()
