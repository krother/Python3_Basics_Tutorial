
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

----

# Comprehensions with numbers

Create the following data structures with one-liners

    # 1. integers
    a = ...
    assert a == [0, 1, 2, 3, 4, 5, 6]

    # 2. squares
    a = ...
    assert a == [0, 1, 4, 9, 16, 25, 36]

    # 3. fractions
    a = ...
    assert a == [1.0, 0.5, 0.33, 0.25, 0.2, 0.17, 0.14]

    # 4. filtering
    a = range(100)
    b = ... a ...
    assert b == [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]

    # 5. dictionary
    a = ...
    assert a == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

    # 6. sum
    a = "123456789"
    b = ... a ...
    assert b == 45

    # 7. x * y
    a = ...
    assert a == [1, 2, 3, 2, 4, 6, 3, 6, 9]

    # 8. nested
    a = ...
    assert a == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

    # 9. random
    # create a list of 10 dice rolls (1..6)

----

## Comprehensions with strings

Solve the following with one-liners

    # 1. flatten the list
    data = ["abc", "def", "ghi"]
    result = ...
    assert result == list("abcdefghi")

    # 2. create all combinations
    first, second = "abc", "de"
    result = ...
    assert result == ['ad', 'ae', 'bd', 'be', 'cd', 'ce']

    # 3. create a dictionary
    result = ...
    assert result == {0: 'A', 1: 'B', 2: 'C'}

    #
    # Use a list of 20k documents for the next exercises
    #
    from sklearn.datasets import fetch_20newsgroups
    import statistics

    docs = fetch_20newsgroups()['data']

    # 4. calculate the length of each document in characters
    result = ...
    assert result[:5] == [721, 858, 1981, 815, 1120]

    # 5. calculate the mean length
    result = ...
    assert round(result, 2) == 1949.31

    # 6. find the shortest document
    result = ...
    assert 'Graphics Library Package' in result

    # 7. find all documents containing the word 'vegetarian'
    result = ...
    assert result[7].startswith('From: DMCOLES@NUACVM.ACNS.NWU.EDU\nSubject: Chicago')

    # 8. extract indices of all documents containing the word 'vegetarian'
    result = ...
    assert 4355 in result

    # 9. extract the first line of each document
    result = ...
    assert result[4] == 'Subject: Re: Shuttle Launch Question'

    # 10. find all unique words starting with 'poly'
    result = ...
    assert len(result) == 50
    assert 'polypropylene' in result


----

# Creating NumPy Arrays

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

----

# NumPy Matrices

Create the following matrices with a few NumPy commands:

    import numpy as np

    # counting
    # array([[ 0,  1,  2,  3],
    #        [ 4,  5,  6,  7],
    #        [ 8,  9, 10, 11],
    #        [12, 13, 14, 15]])

    # counting, columns first
    # array([[ 0,  4,  8, 12],
    #        [ 1,  5,  9, 13],
    #        [ 2,  6, 10, 14],
    #        [ 3,  7, 11, 15]])

    # nested square
    # array([[1, 1, 1, 1],
    #        [1, 0, 0, 1],
    #        [1, 0, 0, 1],
    #        [1, 1, 1, 1]], dtype=uint8)

    # columns
    # array([[0., 1., 2., 3.],
    #        [0., 1., 2., 3.],
    #        [0., 1., 2., 3.],
    #        [0., 1., 2., 3.]])

    # rows
    # array([[0, 0, 0, 0],
    #        [1, 1, 1, 1],
    #        [2, 2, 2, 2],
    #        [3, 3, 3, 3]], dtype=uint8)

    # products
    # array([[0, 0, 0, 0],
    #        [0, 1, 2, 3],
    #        [0, 2, 4, 6],
    #        [0, 3, 6, 9]], dtype=uint8)

    # 2D repeats
    # array([[0, 1, 0, 1],
    #        [2, 3, 2, 3],
    #        [0, 1, 0, 1],
    #        [2, 3, 2, 3]], dtype=uint8)

    # diagonal
    # array([[1, 0, 0, 0],
    #        [0, 1, 0, 0],
    #        [0, 0, 1, 0],
    #        [0, 0, 0, 1]], dtype=uint8

    # triangle
    # array([[1, 0, 0, 0],
    #        [1, 1, 0, 0],
    #        [1, 1, 1, 0],
    #        [1, 1, 1, 1]], dtype=int32)

    # checkerboard
    # array([[1, 0, 1, 0],
    #        [0, 1, 0, 1],
    #        [1, 0, 1, 0],
    #        [0, 1, 0, 1]])

----
