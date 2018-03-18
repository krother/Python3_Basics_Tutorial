
import pylab as plt
import numpy as np
import pandas as pd

xvalues = np.arange(0.0, 20.0, 0.1)

df = pd.DataFrame({
    'x': xvalues,
    'sin': np.sin(xvalues),
})

plt.figure()

df.plot('x', 'sin')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0.0, 20.0, -1.2, 1.2])

plt.title('Sinusfunktion')
plt.savefig('sinusfunktion.png')
