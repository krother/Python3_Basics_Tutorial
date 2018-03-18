
import math
import random
import matplotlib.pyplot as plt

# prepare random data
n_balls = 50
x = [random.triangular() for i in range(n_balls)]
y = [random.gauss(0.5, 0.15) for i in range(n_balls)]
colors = [random.randint(1, 4) for i in range(n_balls)]
areas = [math.pi * random.randint(5, 15)**2 for i in range(n_balls)]

# draw the figure
plt.figure()
plt.scatter(x, y, s=areas, c=colors, alpha=0.75)
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.savefig('streudiagramm.png')
plt.savefig('streudiagramm.svg')
