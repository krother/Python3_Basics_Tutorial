Count Words
===========

In this challenge you can learn:
--------------------------------

==== ==================================
area topic
==== ==================================
🔀    use a counter variable
💡    read a text file
💡    split strings
⚙    use comparison operators
🔧    define absolute and relative paths
🐞    check file names
==== ==================================

The Challenge
-------------

The book *“Moby Dick”* by Herman Melville describes an epic battle of a
gloomy captain against his personal nemesis, the white whale. Who of
them is mentioned in the book more often?

.. figure:: ../images/mobydick_count.png
   :alt: Moby Dick word count

Write a program that counts how often each word occurs in the book.
Determine how often the words ``captain`` and ``whale`` occur. You will
need different data structures for counting words and for sorting them.

When you know whether ``whale`` or ``captain`` occurs more often, you
have mastered this challenge.

The Data
--------

You can find the full text for Herman Melville's “Moby Dick” in the text
file :download:`moby_dick.txt` and on
`www.gutenberg.org <http://www.gutenberg.org>`__.

Hints
-----

Hint 1: What output do you expect?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How should the output of the program look like? Write down a few sample lines of output .


.. hint::

   Output example

   ::

      2307     is
       228     through
         5     tobacco


Hint 2: Find a program structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Which steps should the program execute, and in which order? Draw a small flowchart.

.. hint::

   Program structure
   
   * Read the file.
   * Split it into words.
   * Count each word.
   * Sort the words by counts.
   * Output the words and counts


Hint 3: Finding the right data type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Which data type in Python is suited well to count things?
Which operations on this data type will be necessary to 

* initialize the data type?
* count a word?
* Processing text data

.. hint::

   Dictionaries can be used to count things.

   .. code:: python3

      counter = {}
      counter.setdefault('fish', 0)
      counter['fish'] += 1


Hint 4: Functions
~~~~~~~~~~~~~~~~~
Which Python functions can be used to 

* Read a text file?
* Separate a string into words?

.. hint::

   Reading a text file:

   .. code:: python3

      text = open(filename).read()
   
   chopping up a string:

   .. code:: python3

      list = string.split()


Hint 5: Sorting
~~~~~~~~~~~~~~~

Which data type in Python can be used to sort things?
How would you want to represent words and counts in this data structure?

.. hint::
   
   In Python, lists can be sorted. 
   Lists can contain tuples, e.g.

   .. code:: python3

      my_list = [ (12, 34), (56, 78) ]
      my_list.sort()
   

Hint 6: Sorting by word counts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How does Python sort integers, strings, tuples, and other lists?


.. hint::

   Sorting by word count, not words:
   Try to sort on the command line these lists:

   ::

      [ ( "aaa", 100), ( "bbb", 20) ]
   
   and
   
   ::

      [ ( 100, "aaa"), ( 20, "bbb") ]
   
Hint 7: Did it work?
~~~~~~~~~~~~~~~~~~~~
Where would you expect words like 'is', 'the', 'sea', and 'cerebellum' to occur?
Check whether the output of the program corresponds to your expectations.
Does 'captain' or 'whale' occur more often in the text?

.. hint::

   The first five places should be taken by of (6614),  and (6433), a (4726), to (4625), and in (4173).
   You have to check yourself whether 'whale' or 'captain' is first.


Hint 8: Special characters
~~~~~~~~~~~~~~~~~~~~~~~~~~
Special and uppercase characters may be a problem when separating words.
How can you remove all special characters before starting counting?

.. hint::
   
   Special characters can be removed by the str.replace() function – or more comfortably using the re module.

