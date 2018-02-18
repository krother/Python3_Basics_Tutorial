
from pylab import figure, xticks, bar, savefig,\
                  xlabel, ylabel, title

figure()

x = [1, 2, 3]
y = [115, 11, 259]
labels = ["I", "IV", "VII"]

xticks(x, labels)
bar(x, y)

title('Kosten von Star-Wars-Filmen')
xlabel('Episode')
ylabel('Budget (Mio USD)')

savefig('star_bars.png')
