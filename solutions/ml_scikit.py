
## Machine Learning with Scikit-Learn

Initialize the following dataset:

    from sklearn.datasets import load_wine
    import pandas as pd

    data = load_wine()
    df = pd.DataFrame(data['data'], columns=data['feature_names'])
    X = df.values
    y = data['target']

Complete the following tasks:

    # 1. Split the data into a training and test portion
    from sklearn.model_selection import train_test_split
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)

    # 2. Scale the data
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler().fit(Xtrain)
    Xtrain_sc = scaler.transform(Xtrain)
    Xtest_sc = scaler.transform(Xtest)

    # 3. Train a Linear SVC
    from sklearn.svm import LinearSVC
    svm = LinearSVC(C=1.0).fit(Xtrain_sc, ytrain)

    # 4. Inspect the training accuracy
    svm.score(Xtrain_sc, ytrain)

    # 5. Determine accuracies from a 5-fold cross-validation
    from sklearn.model_selection import cross_val_score
    cross_val_score(svm, Xtrain_sc, ytrain, cv=5)

    # 6. Inspect the test accuracy
    svm.score(Xtest_sc, ytest)

    # 7. Get a prediction for the test set
    ypred = svm.predict(Xtest_sc)

    # 8. Print a confusion matrix for the test set
    from sklearn.metrics import confusion_matrix
    confusion_matrix(ytest, ypred)

    # 9. Calculate confidence scores for each prediction
    prob = svm.decision_function(Xtest_sc)

    # 10. Plot the confidence scores as a histogram
    pd.DataFrame(prob).hist(bins=20, figsize=(18, 12))
