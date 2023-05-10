Loops with for
==============

The ``for`` loop allows you to repeat one or more instructions. To write
a ``for`` loop you need two things: First a **sequence-like
object**\ (e.g. a list, a string, a dictionary or the output of a
function producing sequences). Second, a **variable** that takes
different values as the loop iterates over the sequence. The variable is
easier, because it doesn’t matter what name you give it.

Things you can iterate over with ``for`` loops:

-  strings (character by character)
-  lists
-  dictionaries
-  files (line by line)
-  iterable functions (``range``, ``sorted``, ``reversed``)

Loops with ``for`` are useful whenever you want to repeat instructions a
known number of times, or when you wnat to do something for *all*
elements of a sequence. Below you find some examples.

Loops executing a given number of times
---------------------------------------

With the ``range()`` function, you can set the number of iterations
easily:


.. code:: python3

   for i in range(7):
       print(i)

or using an interval:


.. code:: python3

   for i in range(10, 17):
       print(i)

or backwards:


.. code:: python3

   for i in range(17, 10, -1):
       print(i)

Loops over a string
-------------------

With a string as the sequence, you obtain single characters in each
iteration.


.. code:: python3

   for char in 'ABCD':
       print(char)

Loops over a list
-----------------

A list iterates simply once through each element:


.. code:: python3

   for elem in [1, 22, 333, 4444, 55555]:
       print(elem)

Loops over a dictionary
-----------------------

With a dictionary, the ``for`` loop iterates over the keys. Note that
the dictionary is inherently unordered. Theoretically, you could get the
keys in a different order each time.


.. code:: python3

   pairs = {'Alice': 'Bob', 'Ada': 'Charlie', 'Visual': 'Basic'}
   for key in pairs:
       print(key)
       print(pairs[key])

Looping over two lists simultaneously
-------------------------------------

Sometimes, you want to look up corresponding items from two lists. A
straightforward solution is to loop over an index:


.. code:: python3

   names = ['Alice', 'Bob', 'Charlie', 'Delia']
   jobs = ['admin', 'builder', 'cook', 'developer']

   for i in range(4):
       print(names[i] + ' works as a ' + jobs[i])

However, the *pythonic* solution would be to use ``zip``:


.. code:: python3

   for name, job in zip(names, jobs):
       print(name + ' works as a ' + job)

Indented block
--------------

All indented commands after the colon are executed *within* a ``for``
loop. The first unindented command is executed after the loop finishes.


.. code:: python3

   for i in range(5):
       print('inside')
       print('also inside')
   print('outside')
