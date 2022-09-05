
## Timelines of Baby Names

In this chapter, we would like to know how the popularity of a name changes over time.

To reach that, we will need to wrangle and aggregate the data.

If you want to use the `pandas` library, you find a list of useful functions at the bottom.

## Task 1

Calculate for each name in `yob2000.txt` its percentage of total births. Store this percentage as an additional column.

----

## Task 2

Read all files `yob1880.txt, yob1881.txt ... yob2021.txt`.
Add an extra column for the year.
Concatenate them into a single data structure.

----

## Task 3

Calculate the total number of births for each year.
Visualize the timeline as a line plot.

----

## Task 4

Now, create a timeline for your own name. 
First check if your name occurs at all. If yes, create a table with the columns **year** and **number**.

You may want to sum up the binary genders or choose one. With few exceptions, the influence on the result is tiny.

If your name is not very frequent, there might be missing data for some years.
Insert missing data with a 0.

Draw a line plot and label the axes.

----

## Task 5

Investigate the popularity of the names of some US celebrities over the last 130 years.
Plot a time line with 2-4 names.

Inspect the following celebrities or choose your own:

| name            | comment                        |
|-----------------|--------------------------------|
| Madonna         | wrote "Like a Prayer" |
| Lance           | went to the moon |
| Barack          | president |
| Katrina         | hurricane in New Orleans |
| Luke            | Jedi |
| Leia            | princess from Star Wars |
| Frida           | painter, biography went on a Broadway show |
| Arielle         | mermaid |
| Harley          | it's a chopper |
| Tyrion          | character in 'Game of Thrones' |
| Khaleesi        | job title in 'Game of Thrones' |


----

## Task 6

Finally, we will normalize the data.
Repeat Task 4 or 5, but divide the count of a given name by the total number of births **of that year**.

How does the result change and why is this important?

----

## Useful pandas functions

| function        | comment                        |
|-----------------|--------------------------------|
| `df[new] = value` | create a column filled with the same value |
| `df[new] = df[col] * x` | create a column using arithmetics on an old one |
| `df[new] = df[col].apply(func)` | create a column by calling a function for each value |
| `pd.concat[list]`  | concatenates DataFrames. `list` is a list of DataFrames |
| `df[col].fillna(value, inplace=True)`  | fills missing data |
| `df.groupby(col)`    | splits the DataFrame into multiple sub-DataFrames |
| `df[col].plot()` | create line plots for 1+ columsn |
| `df.set_index(col)`  | moves a column into the index (used for the x-axis in a plot) |
