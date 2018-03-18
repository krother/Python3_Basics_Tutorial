
from pylab import figure, title, xlabel, ylabel, xticks, bar
from pylab import legend, axis, savefig

nucleotides = ["A", "G", "C", "U"]

counts = [
    [606, 1024, 759, 398],
    [762, 912, 639, 591],
]

figure()
title('RNA-Nukleotide im Ribosom')
xlabel('RNA')
ylabel('Anzahl Nukleotide')

x1 = [2.0, 4.0, 6.0, 8.0]
x2 = [x - 0.5 for x in x1]

xticks(x1, nucleotides)

bar(x2, counts[1], width=0.5, color="#87CEEB", label="E.coli 23S")
bar(x1, counts[0], width=0.5, color="#F4A460", label="T.thermophilus 23S")

legend()
axis([0.5, 9.5, 0, 1200])
savefig('balkendiagramm.png')
savefig('balkendiagramm.svg')
