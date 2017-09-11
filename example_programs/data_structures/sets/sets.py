
# things you can do with sets

comedy = set(["Forrest Gump", "Spaceballs", "The 100-year-old.."])
drama = set(["The Godfather", "Heat", "Forrest Gump", "Hamlet"])

print("\nintersection\n", comedy.intersection(drama))
print("\ndifference\n", comedy.difference(drama))
print("\ndifference\n", drama.difference(comedy))
print("\nsym.difference\n", drama.symmetric_difference(comedy))
print("\nunion\n", drama.union(comedy))

