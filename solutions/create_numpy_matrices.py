# NumPy Matrices

# Create the following matrices with a few NumPy commands:

import numpy as np


z = np.ones((4, 4))
z[1:3, 1:3] = 0
z

a = np.arange(4)
a * np.ones((4, 1))

b = a.reshape(4, 1)
b

a * b

c = a.reshape(2,2)
np.tile(c, (2,2))

np.eye(4, 4)

d = np.arange(16).reshape(4,4)
d

d.T

((d - d.T) >= 0).astype(np.int32)

(np.arange(16).reshape(4,4) + np.array([1, 0, 1, 0]).reshape(4,1)) % 2
