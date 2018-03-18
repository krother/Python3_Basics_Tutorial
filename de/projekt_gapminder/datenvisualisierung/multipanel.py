
import pylab as plt
import numpy as np
import pandas as pd

xvalues = np.arange(0.0, 20.0, 0.1)

df = pd.DataFrame({
    'x': xvalues,
    'sin': np.sin(xvalues),
    'cos': np.cos(xvalues),
    'tan': np.tan(xvalues),
    'log': np.log(xvalues),
})

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(df['x'], df['sin'], 'k--')
plt.xlabel('x')
plt.ylabel('$sin(x)$')
plt.axis([0.0, 20.0, -1.2, 1.2])

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(df['x'], df['cos'], 'r^')
plt.xlabel('x')
plt.ylabel('$cos(x)$')
plt.axis([0.0, 20.0, -1.2, 1.2])

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(df['x'], df['tan'], 'g-')
plt.xlabel('x')
plt.ylabel('$tan(x)$')
plt.axis([0.0, 20.0, 0.0, 30.0])

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(df['x'], df['log'], 'bo')
plt.xlabel('x')
plt.ylabel('$log(x)$')
plt.axis([0.0, 20.0, -5, 5.0])

plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.savefig('multipanel.png')
plt.savefig('multipanel.svg')
