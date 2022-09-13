
# Last Letters

**🎯 Analyze which last letters appear most frequently in first names.**

## Task 1

Read all files from the [Baby Name Dataset](http://www.ssa.gov/oact/babynames/limits.html) into a single `DataFrame`. The `DataFrame` should have the columns **name**, **gender**, **number** and **year**.

The following code snippets might be useful (although their order is not):

    df['year'] = year

    df = pd.concat([df1, df2, df3, ...])

    for year in range(1880, 2015):

    dataframes = []


----

## Task 2

Create an extra column with the last letter of each name.

Create string indexes for an entire column with the expression

    :::python3
    df[col].str[i]

Alternatively, write a function that returns the last letter and use it to create a `pd.Series`:

    :::python3
    df[col].apply(my_func)

----

## Task 3

Create a bar plot showing the count of each last letter.

----

## Task 4

Now, create a timeline for one last letter.

First, select that letter over all years.
Second, group by the year and calculate the count for each year.
The resulting table should look like this:

    :::text
    year  count
    1880    300
    1881    317
    1882    342
    ...

Finally, create a line plot from this data.

----

## Task 5

Let's plot multiple timelines.

Count the names grouped by last letter **and** year. Use the expression:

    :::python3
    df.groupby([col1, col2])[col3].count()

The resulting table should look something like this:

    :::text
    last  year
    a     1880    31446
          1881    31581
          1882    36536
    ...
    b     1880     5432

This `DataFrame` has a **hierarchical index**.

Convert the DataFrame to a **crosstable** that has the year in the row index and the letters in the column index.
You can do this with the expression

    :::python3
    df.unstack(0)

Draw a line plot showing the frequency of the letters **d**, **n** and **y**.
Try other ones if you like.

----

## Task 6

Finally, let's look for frequent first/last letter combinations.

1. Add an extra column containing the first letter.
2. Cross-tabulate by grouping by first and last letter and count the names (over all years).

Now you should have a table with first letters in columns an last letters in rows (or vice versa).

Plot a heatmap (check the [Seaborn Example Gallery](http://seaborn.pydata.org/examples/index.html)).

#### Hints:

To make the plot nicer convert the names to upper or lower case at the very beginning with:

    :::python3
    df['name'].str.uppper()


You also might sort the table by rows:

    :::python3
    df.sort_values(by=col, axis=0`)
    
For sorting by columns, set `axis=0`

----

## Task 7

Save your plots to `.png` files with 150 dpi.

----
## Task 8

What visualization(s) would you use to compare the last letters of girls and boys?

----

## Hints:

* Instead of the count, you can use the sum instead.
* You might also try to log-transform the data with `np.log` before plotting.
* It might be a good idea to normalize the data before plotting.
* Of course, the entire analysis also can be done for first letters, but for the last letters a research paper exists that had quite an impact.

*Translated with [www.DeepL.com](www.DeepL.com/Translator)*
