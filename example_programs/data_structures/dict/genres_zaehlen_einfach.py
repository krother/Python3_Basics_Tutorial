"""
Zaehlen von Eintraegen ohne Dictionary

Nachteile:
- Genres muessen bekannt sein
- pro zusaetzliches Genre fallen vier Zeilen an > Fehleranfaelligkeit steigt
- pro Genre linear laengere Laufzeit
"""

scifi = 0
drama = 0

for zeile in open('../moviedb/genres_1000.txt'):
    if "Sci-Fi" in zeile:
        scifi += 1
    elif "Drama" in zeile:
        drama += 1
      
print scifi
print drama
