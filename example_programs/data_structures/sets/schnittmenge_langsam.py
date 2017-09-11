"""
Beispiel wie man eine Schnittmenge nicht berechnen sollte.

Wegen der doppelten for-Schleife waechst die benoetigte Zeit
quadratisch mit der Groesse der Listen an.
"""

komoedie = ["Forrest Gump", "Ziemlich Beste Freunde", "Spaceballs", "Der 100-jaehrige.."]

drama = ["Der Pate", "Heat", "Ziemlich Beste Freunde", "Hamlet", "Forrest Gump"]

print "\nKomische und dramatische Filme:"
for k in komoedie:
    for d in drama:
        if k == d:
            print d

