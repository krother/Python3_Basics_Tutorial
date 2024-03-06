Nested Lists
============

In this chapter you learn:
--------------------------

==== ==============================================
area topic
==== ==============================================
⚙    define a list inside a list
⚙    index a nested list
🔀   loop over a nested list
🔀   create a nested list with a nested loop
==== ==============================================

Data frequently occurs in the form of tables. To process tables in
Python, we can put lists in other lists. These are called **nested lists**:

.. code:: python3

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
E.g. for the third row:

.. code:: python3

   print(table[2])
  
To access a single element, you need two pairs of square brackets.
E.g. for the second column of the third row:

.. code:: python3

   print(table[2][1])

In this chapter we will create and process nested lists.


Exercise 1
----------

Write all rows of the above table to the screen with a ``for`` loop.

Complete the code:

.. code:: python3

   for ... in table:
       print(...):


Exercise 2
----------

Now modify the loop to output only the names.


Exercise 3
----------

Write each individual *cell* of the table to the screen with a nested ``for`` loop.

Complete the code:

.. code:: python3

   for row in ...:
       ... cell in row:
           print(...)


Exercise 4
----------

Create an empty table of 10 x 10 cells and fill them with numbers from 1
to 100.

Sort the lines and indent the code properly:

.. code:: python3

   for x in range(10):
   for y in range(10):
   number = 1
   number += 1
   print(table)
   row = []
   row.append(number)
   table.append(row)
   table = []
