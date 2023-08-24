Data Types in Python
====================


Match the data samples with their types.

.. figure:: datatypes.png
   :alt: datatype exercise

   datatype exercise

========= ========================== ========= =======
data type description                composite mutable
========= ========================== ========= =======
int       integer numbers            no        no
float     floating-point numbers     no        no
string    characters                 no        no
bool      ``True`` or ``False``      no        no
list      sequence of items          yes       yes
tuple     immutable sequence         yes       no
dict      lookup table               yes       yes
set       collection of unique items yes       yes
NoneType  just nothing               no        no
========= ========================== ========= =======

Composite data types
--------------------

Some data types are **composite**, meaning that they may contain objects of other types.
For instance, a `list` can contains strings, numbers or even other lists.

Immutable and mutable data types
--------------------------------

In Python there are basic and composite data types. The values of basic
data types cannot be changed, they are **immutable**. Most of the
composite data types are **mutable**.

--------------

Immutable and mutable data types
--------------------------------

In Python there are basic and composite data types. The values of basic
data types cannot be changed, they are **immutable**. Most of the
composite data types are **mutable**.

The immutable data types in Python are:

-  Boolean (``True`` / ``False``)
-  Integer (``0``, ``1``, ``-3``)
-  Float (``1.0``, ``-0.3``, ``1.2345``)
-  Strings (``'apple'``, ``"banana"``) - both single and double quotes are valid
-  None (aka an empty variable)
-  Tuples (multiple values in parentheses, e.g. \ ``('Jack', 'Smith', 1990)``)

The mutable data types are

-  List [1, 2, 2, 3]
-  Dictionary {‘name’: ‘John Smith’, ‘year’: 1990}
-  Set ()

--------------

Type conversions
----------------

Values can be converted into each other using *conversion functions*.
Try the following:

::

   int('5.5')
   float(5)
   str(5.5)
   list("ABC")
   tuple([1,2,3])
   dict([('A',1),('B',2)])
   set([1,2,2,3])
