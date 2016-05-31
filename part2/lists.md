
# Storing lists of items

To handle larger amounts of data, we cannot invent a new variable for every new data item. Somehow we need to store more data in one variable. This is where Python **lists** come in.


## Exercise 1

Find out what each of the expressions does to the list in the center.

![list exercise](../exercises/lists.png)


## Exercise 2

What does list `b` contain?

    a = [8, 7, 6, 5, 4]
    b = a[2:4]

* `[7, 6, 5]`
* `[7, 6]`
* `[6, 5]`
* `[6, 5, 4]`


## Exercise 3

In the year 2000, a total of 1962406 boys were registered born in the U.S. What percentage of the total names do the top 5 names consist?

You have the following list of the top 10 names:

    top_ten_boys = [34465, 32025, 28569, 27531, \
        24928, 23632, 22818, 22307, 21500]

Write a program that extracts the top 5 names from the list and then calculates the percentage on the 1962406 total births.

#### Hint

If you are using Python2, you need to specify whether you want numbers with decimal places when dividing. That means

    3 / 4 

gives a different result than
 
    3.0 / 4

However, Python 3 automatically creates the decimal places if needed.


## Exercise 4

Use the expressions to modify the list as indicated. Use each expression once.

![list funcs exercise2](../exercises/list_funcs2.png)


## Exercise 5

Use the expressions to modify the list as indicated. Use each expression once.

![list funcs exercise1](../exercises/list_funcs1.png)


## Exercise 6

You have the following two lists:

    top_ten_names = ['Jacob', 'Michael', 'Matthew', 'Joshua', \
        'Christopher', 'Nicholas', 'Andrew', 'Joseph', \
        'Daniel', 'Tyler']

    top_ten_boys = [34465, 32025, 28569, 27531, \
        24928, 23632, 22818, 22307, 21500]

Print a table to the screen with all names in the left column and all numbers in the right column.


## Exercise 7

Create a list that contains the sum of California and New York for each name.

    # Emily, Amy, Penny, Bernadette (2014)
    california = [2269, 542, 54, 21]
    new_york = [881, 179, 12, 11]


## Exercise 8

Read all lines from the file `yob2014.txt` into a list. Print the first 10 and the last 10 lines to the screen.

