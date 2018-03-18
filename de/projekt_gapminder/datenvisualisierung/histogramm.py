
import pylab as plt
import pandas as pd
import random

N_POINTS = 10000
N_BINS = 50

data = [random.gauss(0.0, 1.0) for i in range(N_POINTS)]
s = pd.Series(data)


plt.figure()
plt.hist(s, N_BINS, normed=1.0, histtype='bar',
         facecolor='green', alpha=0.75)

plt.title('Histogramm')
plt.xlabel('Wert')
plt.ylabel('Frequenz')
plt.axis([-5.0, 5.0, 0.0, 0.5])
plt.grid(True)

plt.savefig('histogramm.png')
plt.savefig('histogramm.svg')
