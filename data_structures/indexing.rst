
Indexing and Slicing
====================

Strings and lists are both ordered sequences of elements.
In both, you can address elements by their position.
However, Python is counting differently than humans:

.. figure:: indexing.png
   :alt: Indexing


Exercise 1: slicing strings
--------------------------------

What do the following expressions result in?

.. code:: python3

   name = "hello world"

   name[0]
   name[3]
   name[-1]
   name[0] + name[6]
   name[5:]
   name[5:10]
   name[:10:2]


Exercise 2: Indexing lists
--------------------------

What do the following expressions result in?

.. code:: python3

   numbers = [1, 4, 9, 16, 25, 36]

   numbers[4]
   movies[0]
   movies[-1]
   numbers[-3]


Exercise 3: Slicing
-------------------

What do the following commands result in?

.. code:: python3

   movies = ["Star Wars", "Star Trek", "Ratatouille", "One Piece"]

   movies[2:]

   movies[:2]

   numbers[2:-2]

   numbers[::2]


Exercise 4: Decypher
--------------------

The following text contains an encrypted word:

.. code:: python3

   name = "CSAIPRALKAINACZEYLVOST"

Print every second character, starting with the 2nd).

Exercise 5: Slicing puzzle
--------------------------

Use the expressions to modify the list as indicated. Use each expression
once.

.. figure:: list_funcs1.png
   :alt: list funcs exercise1

   list funcs exercise1


Recap: String manipulation
--------------------------

Fill in the blanks so that the assertions pass

.. code:: python3s

   s = "Hello"

   # 1. Concatenate the string
   ...
   assert s == "Hello World"

   # 2. Convert the string to upper case
   ...
   assert s == "HELLO WORLD"

   # 3. Exract the first word
   ...
   assert s == "HELLO"

   # 4. Capitalize the string
   ...
   assert s == "Hello"

   # 5. Substitute characters
   ...
   assert s == "Hero"
