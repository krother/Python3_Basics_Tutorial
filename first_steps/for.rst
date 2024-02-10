Square Numbers
==============

|image0|

`Image by travelnow.or.crylater on
Unsplash <https://unsplash.com/@travelnow_or_crylater?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText>`__

In this chapter you will:
~~~~~~~~~~~~~~~~~~~~~~~~~

==== =============================
area topic
==== =============================
🚀   calculate square numbers
⚙    use ``for`` loops
⚙    indent instructions
💡   use the ``range()`` function
💡   use the ``time`` module
🐞   recognize bugs at runtime
==== =============================


Exercise 1: Pat your own shoulder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Execute the following program. What happens?

.. code:: python3

   import time

   for i in range(5):
       print("You are great at programming!")
       time.sleep(5)


Exercise 2: Counting
~~~~~~~~~~~~~~~~~~~~

Execute the following two lines:

.. code:: python3

   for number in range(1, 7):
       print(number)

Make the code print the numbers from 1 to 20.


Exercise 3: Prints
~~~~~~~~~~~~~~~~~~

Explain why the ``for``-loop is better than this code sniplet:

.. code:: python3

   print(1)
   print(2)
   print(3)
   print(4)
   print(5)
   print(6)
   print(7)


Exercise 4: Indentation
~~~~~~~~~~~~~~~~~~~~~~~

Explain the difference between the following two programs:

.. code:: python3

   x = 1
   for i in range(10):
       x = x * 2
       print(x)

and

.. code:: python3

   x = 1
   for i in range(10):
       x = x * 2
   print(x)


Exercise 5: Squares
~~~~~~~~~~~~~~~~~~~

Implement a ``for`` loop that produces the following output:

::

   1
   4
   9
   16
   25
   36
   49


Exercise 6: More loops
~~~~~~~~~~~~~~~~~~~~~~

Execute the following loops one by one.

.. code:: python3

   for char in "ABCD":
       print(char)

   for i in range(10):
       print(i)

   for number in [4, 9, 16, 25]:
       print(number)

   for x, y in [(1,2), (3,4), (5,6)]:
       print(x, y)

   rabbits = 10
   for i in range(9):
        rabbits = rabbits + rabbits // 5
        print(rabbits)

.. |image0| image:: squares.jpg

