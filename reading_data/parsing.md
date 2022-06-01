
# Parsing data from text

Most text files contain both text and numbers. Extracting these data fields from a file and storing them in reasonably *structured* variables is called **parsing**. To parse files, we need methods of strings, lists and **type conversions**.


### Exercise 1

Insert the following pieces into the code, so that all commands are executed correctly: `age`, `int(age)`, `name`, `str(born)`, `2000`

    name = 'Emily Smith'
    born = _____
    ____ = '15'

    text = ____ + ' was born in the year ' + _____ + '.'
    year = born + _____
    text
    year


### Exercise 2

The following program collects names in a list that occur at least 10000 times. Unfortunately, the program contains **four errors**. Find and fix these.


    frequent = []

    for line in open('names/yob2015.txt'):
        columns = line.strip().split(',')
        name = colums[1]
        n = int(columns[3])
        if n >= 10000
            frequent.append(name)

    print(frequent)


### Exercise 3

Write a program that calculates the total number of babys for the year 2015 and writes it to the screen. Compare that number with the year 1915.


### Exercise 4

Write a program that finds the *three most frequent* names for boys and girls in a given year and writes them to the screen.

**Hint:** The three most frequent names are on top of the list.


### Exercise 5

Write a program that calculates the percentage of the 10 most frequent names for the year 2015 and writes it to the screen.
