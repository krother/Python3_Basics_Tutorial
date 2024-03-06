Python Programs
===============

A Python program is simply a text file that contains Python statements.

-  All Python programs should have the extension ``.py``
-  Only one command per line is allowed
-  The statementsin the file are interpreted line by line

To execute a Python program, you run it from the command line with:

::

   python my_program.py

For those unfamiliar with the command line all Python editors have
shortcuts to make running a program simpler.

Variables
---------

**Variables** are *‘named containers’* used to store values within
Python. Variable names may be composed of letters, underscores and,
after the first position, also digits. Lowercase letters are common,
uppercase letters are usually used for constants like ``PI``.

Variables can be used for calculating in place of the values they
contain.

Variable assignments
--------------------

The operator ``=`` is used in Python to define a variable. A Python
statement containing an ``=`` is called a **variable assignment**. The
value on the right side of the equal sign will be stored in a variable
with the name on the left side.

Changing variables
------------------

You may assign to the same variable name twice:


.. code:: python3

   In [1]: emily = 25952
   In [2]: emily = 222
   In [3]: emily
   Out[3]: 222

In this case, the first value is overwritten by the second assignment.
There is no way to obtain it afterwards.

Python Statements
-----------------

The lines you are writing all the time are also called Python
**Statements**. A Statement is the smallest executable piece of code.

So far, you have seen at least three different kinds of statements:

-  Calculate a number
-  Put a number into a variable
-  Print the number from a variable on the screen

Reserved words
--------------

Some words like ``import``, ``for`` and ``in`` are called **reserved
words**. They have a special meaning in Python, which means that you
cannont call a variable ``for`` or ``in``. There are 33 reserved words
in Python 3.

You can see the complete list with the commands:


.. code:: python3

   import keyword
   keyword.kwlist

Code blocks and indentation
---------------------------

In Python, **blocks of code** are defined by indentation. They occur
usually after a **control flow statement** (``for``, ``if``) or a
**structural element** (e.g. a function). A code block contains one or
more line that belong to it. Python recognizes this code block by
**indentation**, meaning that each line starts with four extra spaces.
All indented code blocks start with a colon (``:``) at the end of the
line.

Indentation is a central element of Python syntax. Indentation must not
be used for decorative purposes.

Comments
--------

Comments are lines that are *not* executed. They allow you to document
your code to make it easier to read. Also, you can temporarily disable
lines of code. There are different ways to write comments:


.. code:: python3

   # this is a one-line comment

   """This is also a one-line comment"""

   """
   With triple quotes comments can
   stretch over multiple lines.
   """

   '''triple single quotes work like triple double quotes.'''
