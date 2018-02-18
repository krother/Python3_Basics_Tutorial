
from pylab import figure, xticks, plot, savefig,\
                  xlabel, ylabel, title

figure()

x = list(range(1, 11))
y = [8.31, 10.03, 14.22, 13.21, 15.82,
     18.68, 19.96, 19.05, 20.36, 18.99]

plot(x, y, 'b-')

title('Big Bang Facts (Quelle: Wikipedia)')
xlabel('Staffel')
ylabel('Zuschauer (Mio)')

savefig('big_bang_facts.png')
