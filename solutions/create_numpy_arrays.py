"""
Create NumPy arrays using one-liners:
"""
Create the following NumPy arrays using one-liners:

import numpy as np

# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. ])

# array([0, 1, 2, 0, 1, 2, 0, 1, 2, 0])

# array([ 0,  1,  4,  9, 16, 25, 36, 49])

# array([  1,   2,   4,   8,  16,  32,  64, 128, 256])

# array([ 0,  1,  3,  6, 10, 15, 21, 28])

# array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])

# array([1., 1., 1., 1., 0., 0., 1., 1., 1., 1.])

# array([-3.142, -2.094, -1.047,  0.   ,  1.047,  2.094,  3.142])

# array([0.  , 0.69, 1.1 , 1.39, 1.61, 1.79, 1.95, 2.08, 2.2 ])

np.linspace(1.0, 2.0, 6)

np.arange(10)

np.arange(10) % 3

np.arange(8) ** 2

2 ** np.arange(9)

np.cumsum(np.arange(8))

np.repeat(np.array([1,2,3]), 3)

np.hstack([np.ones(4), np.zeros(2), np.ones(4)])

(np.arange(-180, 181, 60) / 180 * np.pi).round(4)
