# Comprehensions with numbers

Create the following data structures with one-liners

[x for x in range(7)]

[x**2 for x in range(7)]

[round(x**0.5, 2) for x in range(7)]

[x for x in range(100) if x**0.5 == int(x**0.5)]

{x: round(x**0.5, 2) for x in range(7)}

sum([int(x) for x in "123456789"])

[x*y for x in range(3) for y in range(3)]

[[x*y for y in range(3)] for x in range(3)]

import random
sorted([random.random() for i in range(10)])

import random
[random.randint(1, 6) for i in range(10)]

#----------------------------------------------

# comprehensions with strings
from sklearn.datasets import fetch_20newsgroups

docs = fetch_20newsgroups()['data']

{x: y for x, y in enumerate('ABC')}

[len(d) for d in docs][:10]

import numpy as np
np.mean([len(d) for d in docs])

[d[:50] for d in docs if 'vegetarian' in d]

[d.split("\n")[1] for d in docs if 'vegetarian' in d]

[i for i, d in enumerate(docs) if 'vegetarian' in d]

{word for d in docs for word in d.split() if word.startswith('poly')}

bla = ["abc", "def"]
[x for y in bla for x in y]

[a+b for a in "abc" for b in "abc"]

min([(len(d), d) for d in docs])[1]
