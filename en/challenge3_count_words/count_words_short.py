import re

r = {}
r.setdefault(0)

for i in open("moby_dick.txt"):
    s = re.findall("[a-zA-z]+", i.lower())
    for t in s:
        if t in r:
            r[t] += 1
        else:
            r[t] = 1
r = sorted(r, key=r.get)
print r[-10:]
		
