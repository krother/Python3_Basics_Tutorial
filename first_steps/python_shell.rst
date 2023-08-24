Python as a Calculator
======================

|image0|

`photograph by Charles Deluvio on
Unsplash <https://unsplash.com/@charlesdeluvio>`__


In this chapter you will:
~~~~~~~~~~~~~~~~~~~~~~~~~

==== ================================
area topic
==== ================================
🚀   use Python as a pocket calculator
💡   use the data type *integer*
⚙    use arithmetical operators (+-*/)
⚙    store numbers in a variable
⚙    change the contents of a variable
🔧   use the Variable Explorer
==== ================================


Arithmetics
-----------

In this chapter we will use the Python console as a pocket calculator.
In Spyder you should see the following prompt (in the bottom right
window):

::

   In [1]:

If you see a different number than 1 it is still the right place.

--------------

Exercise 1: Basic Arithmetics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Execute a few calculations in Python. Insert the missing symbols into
the gaps:

::

   In [1]: 1 + ___
   Out[1]: 3

   In [2]: 12 ___ 8
   Out[2]: 4

   In [3]: ___ * 5
   Out[3]: 20

   In [4]: 21 / 7
   Out[4]: ___

   In [5]: ___ ** 2
   Out[5]: 81

Enter the commands into the console and see what happens.

Do not enter the first part (``In [1]`` etc.). It appears automatically.

--------------

Exercise 2: Division
~~~~~~~~~~~~~~~~~~~~

What is the difference between the following instructions?

.. code:: python3

   10 / 4
   10.0 / 4
   10 // 4
   10 * 0.25

Enter them in the console and examine the result.

--------------

Exercise 3: Operators
~~~~~~~~~~~~~~~~~~~~~

Which operations result in 8?

.. code:: python3

   4 - -4
   65 // 8
   17 % 9
   64 ** 0.5

Enter the instructions and examine the result.

--------------

Exercise 4: Variables
~~~~~~~~~~~~~~~~~~~~~

For saving numbers and results of calculations for later, you can store
them in **variables**.

Fill the gaps:

::

   In [1]: rabbits = 25
   In [2]: cats = 7
   In [3]: raccoons = 5
   In [4]: rabbits
   Out[4]: ...
   In [5]: cats + 1
   Out[5]: ...
   In [6]: 3 * raccoons
   Out[6]: ...

--------------

Exercise 5: Modify Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first instruction modifies the value of a variable from exercise 4.
Insert values and variables so that the result is correct:

::

   In [7]: rabbits = rabbits + 1
   In [8]: rabbits
   Out[8]: ...

   In [9]: animals = ... + ... + ...
   In [10]: animals
   Out[10]: 38

In the **Variable Explorer** in Spyder (top right) you can inspect the
content of each variable.

--------------

Exercise 6: Assignments
~~~~~~~~~~~~~~~~~~~~~~~

Which variable assignmments are correct? Enter the code and execute it
to see if it works.

.. code:: python3

   a = 1 * 2
   2 = 1 + 1
   5 + 6 = y
   seven = 3 * 4

--------------

Exercise 7: Rabbit Multiplication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In April you have 10 rabbits:

.. code:: python3

   rabbits = 10

The rabbits constantly multiply. Every month, their number grows by
**20%**. Therefore, you will have 12 rabbits in May.

**How many rabbits will you have in December?**

Hints:
^^^^^^

-  assume that rabbits never die
-  it is ok to calculate with fractions of rabbits
-  it is ok to copy the same lines multiple times for each month

.. |image0| image:: calculator.png

----

Reflection Questions
~~~~~~~~~~~~~~~~~~~~

* What does the `=` operator do?
* Do you have to initialize every variable before using it?
* How can you swap the values of two variables?
