
# Processing multiple tables

## Exercise 1

The following program calculates the total U.S. births for the last 130 years.

The program contains a **subtle semantic defect**. Run the program and check the output. Find and fix the defect.


    births = []

    print("\nyear    births per year")
    print("-" * 25)
    for year in range(1890, 2015, 10):
        filename = 'names/yob{}.txt'.format(year)
        for line in open(filename):
            columns = line.strip().split(',')
            births.append(int(columns[2]))
        print("{:4d}    {:>8d}".format(year, sum(births)))


## Exercise 2

Write a program that does the following:

* The program asks the user for a name.
* The program reads the file `yob2000.txt`.
* The program prints all lines that contain the entered name.

## Exercise 3

Extend the program to ask for the gender as well. Print only lines that match the gender.

## Exercise 4

Extend the program to read **all** files from 1880 to 2014 and print all lines matching the name.

## Exercise 5

Replace the `input` command by a variable (re-entering the same name over and over should get annoying by now).

## Exercise 6

Collect the numbers for each year in a list. 
Write the resulting list of numbers to an output file.

## Exercise 7

If the name was not found for a given year, use a `0` by default.

## Exercise 8

Instead of matching single names, compare to a list of names (Big Bang or GoT characters).
