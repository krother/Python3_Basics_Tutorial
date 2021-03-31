
# Overfit a Regression Model

For this challenge, import the following modules:

    :::python3
    import numpy as np
    from matplotlib import pyplot as plt
    from sklearn.tree import DecisionTreeRegressor

Solve the following tasks:

    :::python3
    # 1. create an array `X` of 100 floating-point numbers

    # 2. calculate an array `y` as the square of `X` and add some random noise

    # 3. reshape `X` to `(100, 1)`

    # 4. fit a decision tree on `X` and `y`

    # 5. use the model to predict numbers from `X` 

    # 6. plot `y` and `ypred` over `X`

    # 7. vary the amount of noise and the `max_depth` hyperparameter to see overfitting
