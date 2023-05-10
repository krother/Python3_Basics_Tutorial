Data Types in Python
====================

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

Basic and composite data types
------------------------------

**Basic** means that a data type does not contain any other types.
**Composite** means that a data type contains other types.

Immutable and mutable data types
--------------------------------

In Python there are basic and composite data types. The values of basic
data types cannot be changed, they are **immutable**. Most of the
composite data types are **mutable**.

The immutable data types in Python are:

-  Boolean (``True`` / ``False``)
-  Integer (``0``, ``1``, ``-3``)
-  Float (``1.0``, ``-0.3``, ``1.2345``)
-  Strings (``'apple'``, ``"banana"``) - both single and double quotes
   are valid
-  None (aka an empty variable)
-  Tuples (multiple values in parentheses,
   e.g. \ ``('Jack', 'Smith', 1990)``)

The mutable data types are

-  List [1, 2, 2, 3]
-  Dictionary {‘name’: ‘John Smith’, ‘year’: 1990}
-  Set ``{1, 2, 3}``
