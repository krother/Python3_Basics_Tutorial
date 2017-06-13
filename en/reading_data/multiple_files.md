
# Processing multiple files

### Exercise 1

The following program calculates the total number of births during the past 130 years.

The code contains a *subtle semantic bug*. Execute the program. Inspect the output. Find and fix the bug.


    births = []
    result = 0

    print("\nyear    births per year")
    print("-" * 25)
    for year in range(1890, 2015, 1):
        filename = 'names/yob{}.txt'.format(year)
        for line in open(filename):
            spalten = line.strip().split(',')
            births.append(int(spalten[2]))
        print(year, sum(births))
        result += sum(births)
    print("\nResult: {} births total".format(result))


### Exercise 2

Write a program that finds lines containing your name in the years 1880 to 2014.

### Exercise 3

Extend the program in such a way that the gender is being checked as well. Print only lines with matching `'M'` or `'F'`, respectively.

### Exercise 4

Collect all matches in a list.

### Exercise 5

If no matches were found in a given year, add a `0` to the result.
