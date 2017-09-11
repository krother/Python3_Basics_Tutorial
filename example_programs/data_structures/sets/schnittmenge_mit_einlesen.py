"""
Berechnung der Schnittmenge mit Einlesen.
"""

komoedie = []
drama = []

for line in open('../moviedb/genres_1000.txt'):
    col = line.strip().split('\t')
    if col[1] == 'Comedy':
        komoedie.append(col[0])
    elif col[1] == 'Drama':
        drama.append(col[0])
        
komoedie = set(komoedie)
drama = set(drama)

print len(komoedie), len(drama)

print "\nKomische und dramatische Filme:"
print len(komoedie.intersection(drama))

print "\nKomische aber nicht dramatische Filme:"
print len(komoedie.difference(drama))

print "\nDramatische aber nicht komische Filme:"
print len(drama.difference(komoedie))

print "\nKomische *oder* dramatische Filme:"
print len(drama.symmetric_difference(komoedie))

print "\nAlle Filme:"
print len(drama.union(komoedie))

