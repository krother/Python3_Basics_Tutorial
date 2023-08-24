Hello World
===========

In this chapter you will:
~~~~~~~~~~~~~~~~~~~~~~~~~

==== ==============================================
area topic
==== ==============================================
🚀   write a Hello World program in Python
💡   use the *string* data type
💡   call the functions ``print()`` and ``input()``
⚙    store text in a string variable
🔧   enter Python commands
🔧   modify Python commands
🐞   find SyntaxErrors
==== ==============================================


Exercise 1: Your first Program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new file in the **editor window** and enter the following
instructions:

.. code:: python3

   name = input("What is your name? ")
   print("Hello", name)

Execute the program by pressing the **“Execute”** button or pressing
**F5** in Spyder. What happens?

--------------

Exercise 2: Break the program!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When programming, it is inevitable that you make mistakes. Errors can be
simple typos or complicated errors in the logical structure. One of the
most important skills in programming is to find the cause of a bug in a
program and fix it. You can practice this by intentionally breaking the
program and seeing what happens.

Try the following programs with errors one by one and try to understand
the error message:

.. code:: python3

   name = input("What is your name? ")
   pront("Hello", name)

   name = input("What is your name? "
   print("Hello", name)

   name = input("What is your name? ")
   print(Hello , name)

   x = input("What is your name? ")
   print("Hello", x)

How can you find out what is going on?

--------------

Exercise 3: input
~~~~~~~~~~~~~~~~~

Which of the following ``input`` commands work? Try them one by one.

.. code:: python3

   name input("enter your name: ")

   name = input("enter a number: ")

   name = input(enter your name)

   name = input()

--------------

Exercise 4: print
~~~~~~~~~~~~~~~~~

Which of the following ``print`` commands work? Try them one by one.

.. code:: python3

   print "Hello"

   print("Hello", name, name)

   print("Hello" + name)

   print("Hello name")

   print(name)

--------------

Exercise 5: Variable names
~~~~~~~~~~~~~~~~~~~~~~~~~~

Try which of the following names of Python variables can be used:

.. code:: python3

   YODA = 'jedi'

   darth vader = 'sith'

   luke99 = 'jedi' = 'sith'

   2000imperator = 'sith'

   obi_wan_kenobi = 'jedi'

   darth.maul = 'sith'

--------------

Exercise 6: Three little bugs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following program should output a song by Bob Marley.
It contains three bugs.

Find and fix them.

.. code:: python3

   part1 = "Don't worry about a thing"
   part2 = "Cause every little thing"
   part3 = gonna be all right

   text = "part1 + part2 + part3"
   print(text

--------------

Exercise 7
~~~~~~~~~~

Write a program that asks for your first and last name and outputs both.
