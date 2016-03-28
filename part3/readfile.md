
# Reading text files

## Warming up

Match the descriptions with the Python commands.

![file exercise](../exercises/files.png)

## Exercise 1:

Make the program work by inserting `close`, `line`, `yob2014.txt`, `print` into the gaps.

    f = open(___)
    for ____ in f:
        ____(line)
    f.____()

## Exercise 2

Write a program that counts the number of names in the file `yob2014.txt` from the dataset of baby names.

## Exercise 3

Execute the following program. What does it calculate?

    boys = 0
    for line in open('yob2014.txt'):
        if ",M," in line:
            boys = boys + 1

## Exercise 4

How many different names starting with an `M` were there in 2014?

## Exercise 5

How many different *girls* names starting with an `M` were there in 2014?


