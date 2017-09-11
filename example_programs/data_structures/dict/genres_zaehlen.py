"""
Verwenden eines Dictionaries um auszuzaehlen, 
wie oft jedes Genre im Datensatz vorkommt.
"""

filme = [
          ["Forrest Gump", "Drama"],
          ["Forrest Gump", "Komoedie"],
          ["Ziemlich Beste Freunde", "Komoedie"],
          ["Ziemlich Beste Freunde", "Drama"],
          ["Der Pate", "Drama"],
          ["Spaceballs", "Komoedie"],
          ["Der 100-jaehrige..", "Komoedie"],
          ["Heat", "Drama"],
          ["Ziemlich Beste Freunde", "Komoedie"],
          ["Hamlet", "Drama"]
        ]

genres = {}

for zeile in filme:
    name = zeile[0]
    genre = zeile[1]
    genres.setdefault(genre, 0)
    genres[genre] = genres[genre] + 1
    
print "Dramen:", genres["Drama"]
print "Komoedien:", genres["Komoedie"]

