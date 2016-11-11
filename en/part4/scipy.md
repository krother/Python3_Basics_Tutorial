
# scipy

## What is scipy?

`scipy` is a Python library for fitting functions and other kinds of numerical analyses.

## Installation

Write in the command line:

    `pip install scipy`

**Note:** on some machines, this may not work. Especially on Windows, you will need to install e.g. the *Anaconda* distribution to avoid a long and painful struggle.

## Exercises

### Exercise 1

Execute the following program:

    import numpy as np 
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    def func(x, a, b, c):
        return a * np.exp(-(x-b)**2/(2*c**2))

    x = np.linspace(0, 10, 100)
    y = func(x, 1, 5, 2)
    yn = y + .2 * np.random.laplace(size=len(x))

    params, pcov = curve_fit (func, x , yn)
    ys = func(x, params[0], params[1], params[2])

    fig = plt.figure
    plt.plot(x, y, "--")
    plt.show()

### Exercise 2

Add `print` statements to see what the program does.

### Exercise 3

Plot the `y` values with noise added.

### Exercise 4

Plot the `y` values of the best-fit function.

#### Hint:
The `plot` function allows you to use various symbols for plotting, e.g. `^ * . -`.

### Exercise 5

Change the program to generate and fit a linear function instead.


## References

*Code adopted from the O'Reilly book: Scipy and Numpy. See more awesome examples there.*
