import re

r = {}

for i in open("alaeddin.txt"):
    i = i.replace('[', '')
    i = i.replace(']', '')
    s = re.findall("[a-zA-z]+", i.lower())
    for t in s:
        if t in r:
            r[t] += 1
        else:
            r[t] = 1
words = [(r[word], word) for word in r]
words.sort(reverse=True)
print(words[:100])
