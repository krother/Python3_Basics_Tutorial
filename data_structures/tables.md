
# Nested Lists

Data frequently occurs in the form of tables. To process tables in Python, we can put lists in other lists.
These are called **nested lists**:

    table = [
      ["Emma", 20799],
      ["Olivia", 19674],
      ["Sophia", 18490],
      ["Isabella", 16950],
      ["Ava", 15586],
      ["Mia", 13442],
      ["Emily", 12562],
    ]

Generally, for nested lists, the same rules apply as for single lists.
To access a single element, you need two pairs of square brackets, e.g. for the second column of the third row:

    print(tab[2][1])


In this chapter we will create and process nested lists.

----

## Exercise 1

Write all rows of the above table to the screen with a `for` loop.

Complete the code:

    for ... in table:
        print(...):

----

## Exercise 2

Now modify the loop to output only the names.

----

## Exercise 3

Write all *cells* of the table to the screen with a nested `for` loop.

Complete the code:

    for row in ...:
        ... cell in row:
            print(...)

----

## Exercise 4

Create an empty table of 10 x 10 cells and fill them with numbers from 1 to 100.

Sort the lines and indent the code properly:

    for x in range(10):
    for y in range(10):
    number = 1
    number += 1
    print(table)
    row = []
    row.append(number)
    table.append(row)
    table = []
    
