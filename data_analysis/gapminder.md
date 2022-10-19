
# Life Expectancy Animation

In this Step, you will create an animated scatterplot on global demography
similar to the one in a famous [talk by Hans Rosling](https://www.youtube.com/watch?v=jbkSRLYSojo).

## Step 1: Download the Data

You will use data by the [Gapminder Foundation](http://www.gapminder.org).
Go to [www.gapminder.org/data](http://www.gapminder.org/data) and download CSV files on:

* life expectancy
* fertility rate, total
* population

----

## Step 2

Load all three tables. Make sure the data is correct:

* inspect the dimensions you should have 200+ rows and 60+ columns.
* make sure the country names are in the **row index**
* make sure the years are in the **column index**
* use `df.columns` to check whether the column index consists of strings or integers (both are ok but you need to know)

----

## Step 3

Choose fertility and life expectancy for the year 2015 and put them into a single table.

----

## Step 4

Remove all rows with missing values.

----

## Step 5

Draw a scatterplot of fertility over life expectancy in 2015.

----

## Step 6

Repeat steps 3-5 for the year 1960. What differences do you observe?

Ideally, format the axes of both plots so that they are the same.
This can be done (e.g. with `plt.axes([left, bottom, width, height])`).

----

## Step 7

Write a function that allows you to draw a scatterplot for any given year.

----

## Step 8

Create one scatterplot for each year from 1960 to 2010 and write it to a file.

----

## Step 9

Connect the scatterplots to an animation.

You can use the `imageio` module.
Install it with:

    :::bash
    pip install imageio

Then adapt and run the code:

    :::python3
    import imageio

    plots = [
        imageio.imread(f'myplot_{year}.png'))
        for year in range(___, ___)
    ]

    imageio.mimsave('animation.gif', plots, fps=20)


----

## Step 10

Also read the population file.
Because the population is written like **500k** or **20M**, you need a conversion function that converts a single value:

    :::python3
    def pop_convert(x):
        if pop.endswith('k'):
            return int(pop[:-1]) * 100_000
        ...

Use the `df.apply()` function to convert the entire DataFrame or a single column:

    :::python3
    df.apply(pop_convert)

----

## Step 11

Divide the population by `100_000`. 
Use the population to control the size of the bubbles in the scatterplot (`df.plot.scatter` accepts an argument `s` of the type `pd.Series`).

----

## Step 12

Let's color by continent:

Read a list of country-continent pairs (:::file continents.csv ).

* Create an extra continent column. 
* Ignore countries for which the continent information does not fit (probably because of spelling).
* Use the continents to color the scatterplot bubbles by continent.

#### Hint:

In matplotlib, this is very tedious. You may need to convert the continents to integers starting from 0.
With `seaborn` it is **a lot easier**.

----

## Step 13

If you use the data on your website or GitHub profile, please copy the license remark from the Gapminder page.
