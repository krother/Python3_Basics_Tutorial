
from collections import Counter

seq = "AAGCTATGGCATATCGAGTACGGACCC"

dna = Counter(seq)

#dna = Counter()
#for s in seq:
#    dna[s] += 1

print(dna.most_common(4))
