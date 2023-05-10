Conditional loops with while
============================

Another control flow statement is the **conditional loop** with
``while``. While loops combine the properties ``for`` and ``if``. The
loop is executed as long as the conditional expression at the beginning
holds. The conditional expressions work in exactly the same way as in
``if`` statements.

Counting until a certain value
------------------------------

A simple usage of while is to count until an exit condition is met. The
following loop calculates the sum of all numbers from 1 through 10:


.. code:: python3

   i = 0
   total = 0
   while i < 10:
       print(i)
       i = i + 1
       total = total + i

Searching through data
----------------------

With a ``while`` loop you can perform search operations - although many
times the methods on lists and dictionaries will give you a shortcut.

The following loop finds the first name starting with an ``'E'``:


.. code:: python3

   data = ['Alice', 'Bob', 'Charlie', 'Emily', 'Fred']
   i = 0
   while i < len(data) and not data[i].startswith('E'):
       i += 1
   print(i)

Waiting for user input
----------------------

A ``while`` loop is also useful to let a user stop the program:


.. code:: python3

   number = 0
   while input('press [Enter] to continue or [x] to exit') != 'x':
       number = number +1
       print(number)

Endless loops
-------------

With ``while`` it is possible to build loops that never stop. Most of
the time this happens by accident. In the following loop, the
instruction to decrease ``a`` is missing. It runs endlessly:


.. code:: python3

   a = 10
   b = 1
   while a > 0:
       b = 1 - b
       print(b)
