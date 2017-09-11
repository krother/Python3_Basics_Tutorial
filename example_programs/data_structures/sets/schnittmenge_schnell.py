
komoedie = set(["Forrest Gump", "Ziemlich Beste Freunde", "Spaceballs", "Der 100-jaehrige.."])

drama = set(["Der Pate", "Heat", "Ziemlich Beste Freunde", "Hamlet", "Forrest Gump"])

print "\nKomische und dramatische Filme:"
print komoedie.intersection(drama)

print "\nKomische aber nicht dramatische Filme:"
print komoedie.difference(drama)

print "\nDramatische aber nicht komische Filme:"
print drama.difference(komoedie)

print "\nKomische *oder* dramatische Filme:"
print drama.symmetric_difference(komoedie)

print "\nAlle Filme:"
print drama.union(komoedie)

