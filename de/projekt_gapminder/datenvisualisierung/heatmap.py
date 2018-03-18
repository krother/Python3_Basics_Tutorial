
import pylab as plt
import numpy as np

a = np.arange(-4, 4, 0.1)
x, y = np.meshgrid(a, a)
matrix = np.sin(x**2 + y**2)

plt.figure()

plt.imshow(matrix, cmap=plt.cm.plasma)  # gray, hot, magma, ..
plt.colorbar()

plt.title("Heatmap der Funktion $\sin{(x^2 + y^2)}$")

plt.savefig("heatmap.png")
plt.savefig("heatmap.svg")
