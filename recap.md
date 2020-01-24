
# Recap Exercises

## String manipulation

Fill in the blanks so that the assertions pass

    s = "Hello"

    # 1. Concatenate the string
    ...
    assert s == "Hello World"

    # 2. Convert the string to upper case
    ...
    assert s == "HELLO WORLD"

    # 3. Exract the first word
    ...
    assert s == "HELLO"

    # 4. Capitalize the string
    ...
    assert s == "Hello"

    # 5. Substitute characters
    ...
    assert s == "Hero"

----

## Reading and Writing Text Files

Complete the following tasks **wihout using pandas/numpy**

    # 1. Create a list with the numbers 1..7

    # 2. Convert the numbers to a string

    # 3. Open a file for writing

    # 4. Write the numbers to the file

    # 5. Make sure the file is closed

    # 6. Open the file for reading

    # 7. Loop over the file object

    # 8. Collect all numbers in a list

    # 9. Sum up the numbers

    # 10. Append the sum as an extra line to the same file

----

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

    # 2. Scale the data

    # 3. Train a Linear SVC

    # 4. Inspect the training accuracy

    # 5. Determine accuracies from a 5-fold cross-validation

    # 6. Inspect the test accuracy

    # 7. Get a prediction for the test set

    # 8. Print a confusion matrix for the test set

    # 9. Calculate confidence scores for each prediction

    # 10. Plot the confidence scores as a histogram


----

## Format Strings

Define the variables:

    label = "knights"
    n = 12  # number by John Dryden, not Monty Python
    mean = 1.2345678

Produce the following strings using the data from the variables

    "12"

    "knights: 12"

    "KNI: 12"

    "There are 12 knights of the table round"

    "knights   :    12"

    "   knights:    12"

    "knights   : 00012"

    """knights
    12
    1.2345678"""

    "1.23"   1.

    "  1.2345678000"
