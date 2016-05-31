
# Working with directories

To process bigger amounts of data, you will need to work on more than one file. Sometimes you don't know all the files in advance.

## Warming up

Fill in the gaps

![os exercise](../exercises/os.png)

## Exercise 1

Explain the following code:

    import os
    for dirname in os.listdir('.'):
        print(dirname)


## Exercise 1

Write a program that counts the number of files in the unzipped set of baby names. Have the program print that number.

Verify that the number is correct.

## Exercise 2

How many entries (lines) does the entire name dataset have?

**Hint**: Generate a message that tells you which file the program is reading.

## Exercise 3

Write a program that finds the *most frequently occuring name* in each year and prints it.

## The Challenge

Find and print your name and the according number in each of the files, so that you can see how the number changes over time.
