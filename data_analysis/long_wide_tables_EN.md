
# Long vs Wide Table Format

![](long_vs_wide.png)

In this exercise we will examine the correlation of life expectancy and fertility.
For this purpose, we will create a scatterplot for the year 2015.

### Step 1

Load the file `gapminder_fertility.csv` into pandas.

    import pandas as pd

    fert = pd.read_csv('gapminder_total_fertility.csv', index_col=0)

### Step 2

Proceed in the same way with the file `gapminder_lifeexpectancy.xlsx`. Save it in a `DataFrame` with the name `life`.

**You need the function `pd.read_excel`.**

### Step 3

Check whether both tables have the same size and shape.

    print(life.shape)

**If they don't, it is not a problem.**

### Step 4

Take a look at the columns of both tables:

    fert.columns

and

    life.columns

One table has columns as strings, the other has integer numbers. To merge the tables, we need to convert both into the same format. First, we create a list of years as integers.

    ncol = [int(x) for x in fert.columns]

and use this list as the new columns:

    fert.set_axis(axis=1, labels=ncol)

Check with `fert.columns` whether the transformation was successful.


### Step 5

Join both tables with the `merge` function. With the parameters `left_index=True, right_index=True` rows with the same indices will be joined.

    df = life.merge(fert, left_index=True, right_index=True)

Check `df.columns`. What happened?

### Step 6

To obtain nice column names, you can also create a **hierarchical index**. For that, we convert both tables to the *long format*:

    sfert = fert.stack()
    slife = life.stack()

The variables `sfert` and `slife` now have the type `pd.Series`. Multiple Series can be converted to a `pd.DataFrame`, using a dictionary with the values:

    d = {'fertility': sfert, 'lifeexp': slife}
    df2 = pd.DataFrame(data=d)

This huge table is easier to convert to the right format, if we first interpret all indices (rows and columns) as row indices:

    df3 = df2.stack()

Finally we can convert the *long* table back to a *wide* one. For that we create new columns from the 1st and 3rd level of the index (the country names and attributes):

   df4 = df3.unstack((0,2))

The zero stands for the first element of an index. With the value 1 all year numbers would end up as columns.

Now `df4` is a table, with years on the left side and life expectancy and fertility for a ll countries on top.

### Step 7

Now you can select specific columns and plot them:

    import pylab as plt
    df4[['Germany', 'France', 'Sweden']].plot()

To create a scatterplot, we extract the columns to plot from  `df3`:

    df5 = df3.unstack(2)
    df5.plot.scatter('fertility', 'lifeexp', s=0.1)

Using `stack` and `unstack` you can also select a year. That makes the plot easier to read:

    df6 = df3.unstack(1)
    df6 = df6[1950]     
    df6 = df6.unstack(1)
    df6.plot.scatter('fertility', 'lifeexp', s=0.1)

### Step 8

Now we can improve our graphics, e.g. color each country differently:

    cmap = plt.get_cmap('tab20').colors
    df6.plot.scatter('fertility', 'lifeexp', s=0.1, c=cmap)

or use a third column with the size of the dots:

    df6.plot.scatter('fertility', 'lifeexp', s=df6['population'])
