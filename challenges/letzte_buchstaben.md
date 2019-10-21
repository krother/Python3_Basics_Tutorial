
# Last Letters

**🎯 Analyze which last letters appear most frequently in first names.**

## Task 1

Read all files from the [Baby Name Dataset](http://www.ssa.gov/oact/babynames/limits.html) into a single `DataFrame`. The `DataFrame` should have the columns **Name**, **Gender**, **Number** and **Year**. The following code snippets could be useful:

    df['year'] = year

    df = pd.concat([df1, df2, df3, ...])

    for year in range(1880, 2015):

    jahrgaenge = []


## Task 2

Write a function that returns the last letter. Add a new column with the last letter to the DataFrame. Use `df.apply` to do this.

## Task 3

Calculate the sum of the first names grouped by gender, last letter and year. The resulting table should look something like this:

    gender  last  year
    F       a     1880    31446
                  1881    31581
                  1882    36536

This `DataFrame` has a **hierarchical index**.

## Task 4

Now calculate the **proportion of a first name within a year** for boys. Unfortunately, the three commands have been mixed up. Find out the correct order:

    df = df / df.sum()
    df = df.unstack()
    df = df.ix['M']

### Hints:

The final letter `a` had a ratio of 0.007023 in 1880.

## Task 5

Select the years **1910** and **2010**. Draw a bar chart with a group of bars for each letter, consisting of two bars for each year.

## Task 6

Select the final letters **d**, **n** and **y**. Draw a line chart showing the frequency of these letters over time.

## Task 7

How have the final letters changed in the last century?

## Task 8

Is there a similar effect for girls?


*Translated with [www.DeepL.com](www.DeepL.com/Translator)*
