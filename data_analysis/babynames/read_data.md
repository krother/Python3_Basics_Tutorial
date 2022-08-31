
# Read Baby Name Data

![Babynamen](../images/baby.png)

The US authorities have registered the names of all US citizens born since 1880. The record is [publicly available](http://www.ssa.gov/oact/babynames/limits.html).

In this and the following chapters, you will to analyze this data.
If you want to use the `pandas` library, you find a list of useful functions at the bottom.

## Preparations

* Download the dataset of US baby names from [www.ssa.gov/oact/babynames/limits.html](https://www.ssa.gov/oact/babynames/limits.html) 
* start with the **national data**
* Unzip the file

## Disclaimer

To protect individuals, only name/gender combinations that occur at least 5 times are listed in the data record.
Also, the table contains genders assigned at birth. Although more genders exist, only two of them are in the data.

----

## Task 1

Inspect the file **yob2021.txt** in a text editor.
What do you observe about the structure of the file?

Usually these questions are the most relevant:

* How many columns are there?
* How are columns separated?
* Is there a header on top of the files?

----

## Task 2

Read the file **'yob2021.txt'** into pandas.

----

## Task 3

Print the first 10 rows.

----

## Task 4

Display the number of rows and columns.

----

## Task 5

Calculate the total number of babies born in 2021, i.e. the sum of the third column.

----

## Task 6

Like Task 5, but calculate the sum for boys and girls separately.

----

## Task 7

Check if your name occurs in the data.

----

## Task 8

Calculate the percentage of girls and boys among the total births.

----

## Task 9

Create a table that contains the top 5 girls names and top 5 boys names.

----

## Task 10

Write the data from task 9 to an Excel spreadsheet.

----

## Useful pandas functions

| function        | comment                        |
|-----------------|--------------------------------|
| `pd.read_csv()` | set `index_col` to 0 or 1 |
| `df.head(x)`    | `x` is a number |
| `df.shape`    | this is an attribute, not a method |
| `df.sum()`    | also try to select a column first |
| `df[df[col] == x]` | selection logic |
| `pd.concat[list]`  | `list` is a list of DataFrames |
| `df.to_excel(fn)`  | `fn` is a path/filename |
