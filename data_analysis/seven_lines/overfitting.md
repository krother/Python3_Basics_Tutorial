
# Overfit a Regression Model

For this challenge, import the following modules:

    :::python3
    import numpy as np
    from matplotlib import pyplot as plt
    from sklearn.tree import DecisionTreeRegressor

Solve the following tasks:


----

## Task 1
Create an array `X` of 100 floating-point numbers

----

## Task 2
Calculate an array `y` as the square of `X` and add some random noise

----

## Task 3
Reshape `X` to `(100, 1)`

----

## Task 4
Fit a decision tree on `X` and `y`

----

## Task 5
Use the model to predict numbers from `X` 

----

## Task 6
Plot `y` and `ypred` over `X`

----

## Task 7
Vary the amount of noise and the `max_depth` hyperparameter to see overfitting