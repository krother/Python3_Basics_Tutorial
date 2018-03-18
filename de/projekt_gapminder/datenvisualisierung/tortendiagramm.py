
from pylab import figure, title, pie, savefig

nucleotides = 'G', 'C', 'A', 'U'
count = [1024, 759, 606, 398]
explode = [0.0, 0.0, 0.05, 0.05]

colors = ["yellowgreen", "limegreen", "orchid", "mediumorchid"]


def get_percent(value):
    '''Formats float values in pie slices to percent.'''
    return "%4.1f%%" % (value)


figure()
title('Nukleotide in der 23S RNA aus T.thermophilus')

pie(count, explode=explode, labels=nucleotides, shadow=True,
    colors=colors, autopct=get_percent)

savefig('tortendiagramm.png', dpi=150)
savefig('tortendiagramm.svg', dpi=150)
