
# Tables

Data frequently occurs in the form of tables. To process tables in Python, it helps to know that we can put lists in other lists. These are also called **nested lists**. 

A simple table in Python looks like this:

    # columns: Name, #California, #New York
    [
      ["Emily", 2269, 881],
      ["Amy", 542, 179],
      ["Penny", 54, 12],
      ["Bernadette", 21, 11]
    ]

In this chapter we will deal with creating and processing nested lists.


### Exercise 1

Write all rows of the above table to the screen with a `for` loop.


### Exercise 2

Write all *cells* of the table to the screen with a double `for` loop.


### Exercise 3

Create an empty table of 10 x 10 cells and fill them with numbers from 1 to 100.


### Exercise 4

Sort the above table by the second column. Use the following code sniplet:

    from operator import itemgetter
    tabelle.sort(key=itemgetter(col_index))
