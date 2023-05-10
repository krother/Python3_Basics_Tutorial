Tuples
======

A tuple is a sequence of elements that cannot be modified. They are
useful to group elements of different type.


.. code:: python3

   person = ('Emily', 'Smith', 23)

In contrast to lists, tuples can also be used as **keys** in
dictionaries.

Indexing tuples
---------------

Elements of tuples can be indexed in the same way as lists:


.. code:: python3

   person[0]
   person[-2]
   person[1:]

Iterating over tuples
---------------------

You can run a ``for`` loop over a tuple:


.. code:: python3

   for elem in person:
       print(elem)

Packing and unpacking tuples
----------------------------

Enumerating multiple values separated by a comma implictly creates
tuples:


.. code:: python3

   person = 'Emily', 'Smith', 23

Tuples can be unpacked to multiple variables:


.. code:: python3

   first, last, age = person

It is even possible to swap the value of variables that way:


.. code:: python3

   first, last = last, first
