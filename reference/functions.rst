Functions
=========

What is a function?
-------------------

A function is an autonomous sub-program with local variables, input and
output. Functions help you divide a program into smaller logical
portions. It is much easier to write, reuse and debug a program
consisting of many small functions than a single huge blob of code.

In Python, a function definition must be followed by a code block:


.. code:: python3

   def calc_price(fruit, n):
       '''Returns the price of fruits.'''
       if fruit == 'banana':
           return 0.75 * n

   print(calc_price('banana', 10))

Obligatory and optional parameters
----------------------------------

Each function can have **obligatory** parameters (that *must* be given
when calling the function and **optional** parameters that have default
values. The following function can be called in two ways:


.. code:: python3

   def calc_price(fruit, n=1):
       '''Returns the price of fruits.'''
       if fruit == 'banana':
           return 0.75 * n

   print(calc_prices('banana'))
   print(calc_prices('banana', 100))

Warning
^^^^^^^

Do not use *mutable* default values (e.g. lists and dictionaries) in the
function header. They make a mess!

List and keyword parameters
---------------------------

For even greater flexibility with function parameters you can also add a
list ``*args`` for an unspecified number of extra parameters, or a
dictionary ``**kwargs`` for keyword parameters.


.. code:: python3

   def func(*args, **kwargs):
       print(args[1])
       print(kwargs['a'])

   func(1, 2, a=3, b=4)

This example may be a bit hard to digest, but these kinds of parameters
are used widely.

Return values
-------------

A function may return values to the program part that called it.


.. code:: python3

   return 0.75

Multiple values are returned as a tuple.


.. code:: python3

   return 'banana', 0.75

In any case, the ``return`` statement ends the execution of a function.
Nothing speaks against having multiple ``return`` statements in a
function (although for clarity it should not be too many).
