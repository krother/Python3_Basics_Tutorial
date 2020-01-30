
# Comprehensions with strings

# Solve the following with one-liners

# 1. flatten the list
data = ["abc", "def", "ghi"]
result = [x for y in bla for x in y]
assert result == list("abcdefghi")

# 2. create all combinations
first, second = "abc", "de"
result = [a+b for a in first for b in second]
assert result == ['ad', 'ae', 'bd', 'be', 'cd', 'ce']

# 3. create a dictionary
result = {x: y for x, y in enumerate('ABC')}
assert result == {0: 'A', 1: 'B', 2: 'C'}

#
# Use a list of 20k documents for the next exercises
#
from sklearn.datasets import fetch_20newsgroups
import statistics

docs = fetch_20newsgroups()['data']

# 4. calculate the length of each document in characters
result = [len(d) for d in docs]
assert result[:5] == [721, 858, 1981, 815, 1120]

# 5. calculate the mean length
result = statistics.mean([len(d) for d in docs])
assert round(result, 2) == 1949.31

# 6. find the shortest document
result = min([(len(d), d) for d in docs])[1]
assert 'Graphics Library Package' in result

# 7. find all documents containing the word 'vegetarian'
result = [d[:50] for d in docs if 'vegetarian' in d]
assert result[7].startswith('From: DMCOLES@NUACVM.ACNS.NWU.EDU\nSubject: Chicago')

# 8. extract indices of all documents containing the word 'vegetarian'
result = [i for i, d in enumerate(docs) if 'vegetarian' in d]
assert 4355 in result

# 9. extract the first line of each document
result = [d.split("\n")[1] for d in docs]
assert result[4] == 'Subject: Re: Shuttle Launch Question'


# 10. find all unique words starting with 'poly'
result = {word for d in docs for word in d.split() if word.startswith('poly')}
assert len(result) == 50
assert 'polypropylene' in result
