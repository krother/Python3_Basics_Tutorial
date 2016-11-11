
# pandas

## What is pandas?

`pandas` is a Python library for efficient handling of tables.

## Installation

Write in the command line:

    `pip install pandas`

## Exercises

### Exercise 1

Execute the following program:

    import pandas as pd
    
    girls = []
    for year in range(1880, 2015):
        fn = "names/yob%i.txt" % year
        df = pd.read_csv(PATH + fn, names=['gender', year], index_col=0)
        girl = df[df.gender=='F'][year]
        girls.append(girl)

    girls = pd.DataFrame(girls).fillna(0)

### Exercise 2

Write the content of the variables to the screen by adding `print` statements. Explain what it does.


### Exercise 3

Add the following lines to the program. Explain them.

    tgirls = girls.transpose()
    tgirls['sum'] = girls.apply(sum)

### Exercise 4

Add the following lines to the program. Explain them.

    tgirls = tgirls[tgirls['sum'] >= 1000]
    tgirls.to_csv('girls_1000.csv')

### Exercise 5

Add lines to conduct a similar analysis of boys' names.
