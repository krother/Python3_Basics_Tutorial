
# Collections: Shortcuts for using dictionaries/lists

from collections import Counter
from random import choice

names = ["Adam", "Bea", "Charlie", "Danielle", "Eve", "Frantz", "Gustav", "Helena"]

# generate 100 random names
data = [choice(names) for i in range(100)]

c = Counter(data)

print(c)
print(c.most_common(3))
