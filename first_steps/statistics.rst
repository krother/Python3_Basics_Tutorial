Statistics
==========

Writing all instructions into a single sequence creates programs that
are hard to debug. Here, you learn to break the code down into smaller
units: **functions**.

In this chapter you learn:
--------------------------

==== ==============================================
area topic
==== ==============================================
🚀   calculate statistics
⚙    implement a function
⚙    call a function you defined
💡   use the ``math`` module
💡   use the ``sum`` function
🔀   use a recursive function
==== ==============================================


Exercise 1: Sum up
------------------

Write a function that calculates a sum from a list of numers. Insert
into the gaps: ``numbers``, ``data``, ``def``, ``return``,
``calc_sum',``\ +=\`

.. code:: python3

   ____ calc_sum(data):
       total = 0
       for n in ____:
           total ____ n
       ____ total

   numbers = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]
   s = ____(____)
   print(s)


Exercise 2: Mean
----------------

Write a function that calculates the arithmetic mean from the following numbers:

.. code:: python3

   def mean(data):
       ...

   numbers = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]

   ...

Don't forget about the ``return`` statement.


Exercise 3: Shortcut
--------------------

Simplify the mean function using the function ``sum()``.

Use your own or the builtin ``sum()`` function.


Exercise 4: Standard Deviation
------------------------------

The following program calculates the standard deviation from a list of
numbers. You would like to generalize the code, so that it can be used
with other data sets. Wrap the code for the calculation – but not the
data – in a function.

.. code:: python3

   import math

   data = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]

   avg = mean(data)

   stdsum = 0.0
   for n in data:
       stdsum += (n - avg) ** 2
   variance = stdsum / len(data)
   stdev = math.sqrt(variance)

   print(f"Standard Deviation: {stdev:8.2f}")


Exercise 5: Optional Parameters
-------------------------------

Explain the program:

.. code:: python3

   def add(a=2, b=2):
       return a + b

   print(add(3, 3))
   print(add(3))
   print(add())
   print(add(b=4))


Exercise 6: Recursion
---------------------

Explain the code:

.. code:: python3

   def factorial(n):
       """Calculates the factorial of the given number."""
       if n > 1:
           return n * factorial(n - 1)
       else:
           return 1


   x = int(input('Please enter a number: '))
   y = factorial(x)
   print (f"The result is:\n{x}! = {y}}")


Reflection Questions
--------------------

-  Why is it useful to write functions?
-  What do you need to write in a function definition?
-  How do you call a function?
-  What does the ``return`` statement do?
