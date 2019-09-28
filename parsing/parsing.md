
# Parsing data from text files


## Exercise 1

Find out what each of the expressions does to the string in the center.

![string exercise](../images/strings.png)


## Exercise 2

The following program identifies names that occur at least 10000 times and collects them in a list.

The program **contains 3 defects**. Find and correct them.


    frequent = []

    for line in open('names/yob2000.txt'):
        columns = line.strip().split(',')
        name = columns[1]
        number = int(columns[3])
        if number >= 10000
            frequent.append(name)

    print(freqent)


## Exercise 3

Create a text file with the contents:

    Alice Smith;23;Macroeconomics
    Bob Smith;22;Chemistry
    Charlie Parker;77;Jazz

Write a program that reads all names and puts them into a list. Print the list.


## Exercise 4

Collect the names and occupations from the above file in two separate lists.


## Exercise 5

Leave the `strip()` command away from the above program. What happens?


## Exercise 6

Write a program that finds out how often your own name occurs in the list of 2014 baby names and print that number.
