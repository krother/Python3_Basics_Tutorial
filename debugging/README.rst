
Twenty Questions
================

In this chapter you will:
-------------------------

==== ==============================================
area topic
==== ==============================================
🚀   get the question-answer game to work
💡   load a JSON file
🔧   work with a minimal input file
🐞   check code for errors
🐞   read error messages
🐞   add diagnostic print statements
==== ==============================================

Exercise 1: Execute the program
-------------------------------

Below you find the code for the game **twenty questions**.
In the game, you think of an animal.
The computer tries to guess it using only yes/no questions.

To get started:

- download the code :download:`twenty_questions.py`
- download the questions in :download:`questions.json`
- place both in the same folder
- execute the program

What happens?

Here is the complete code:

.. literalinclude:: twenty_questions.py

Exercise 2: Read the code
-------------------------

The easiest type of bugs are **Syntax Errors**.
A Syntax Error generally means that the code is not understandable
for the Python interpreter, so it refuses to execute any of it.

This type of bug is the easiest to fix.
Actually, your editor should find all Syntax Errors for you.

Find and fix them.


Exercise 3: Read error messages
-------------------------------

Once you fixed all Syntax Errors, Python starts executing code.
The next type of bug are errors that occur *while the program runs*.
These are called **Exceptions at Runtime**.
The program terminates, and you see an error message – so you know there is a bug.

What can you learn about an errors from reading the error messages?
Try to fix the errors as good as you can.

.. hint::

   A good practice when debugging Python code is to read error messages *from the bottom*.

Exercise 4: Diagnostic prints
-----------------------------

Many bugs do not produce an error message.
To Python everything looks fine.
But you notice that the program is not doing what it should.
This category, **Semantic Errors** is harder to identify,
because you need to find out *that* something goes wrong and then *what* exactly goees wrong.

With a semantic error, you might want to add extra ``print`` statements to your program
so that you can learn what is happening.
Such a *diagnostic print* could be as simple as:

.. code:: python3

   print("reached AAA")

or display the contents of a variable:

.. code:: python3

   print(finished)

Inspect the next bug using an extra ``print``.
Remove the ``print`` if it helps you to fix the bug.

Exercise 5: Minimal input
-------------------------

If your program works with lots of data, debugging is more difficult.
One problem with the game is that the JSON file ``questions.json`` 
contains a couple of thousand questions.

Let's use a simpler one.

Create a file ``mini_questions.json`` and use it instead by changing the file name in the program.
It should contain the following minimalistic data:

::

    {
      "text": "is it a Python?",
      "yes": {
               "text": "it is a Python!"
               },
      "no": {
               "text": "it is some other animal."
               }
    }

If you get the game to work with this data,
switch back to the bigger file.

**Good luck!**

Reflection Questions
--------------------

* what types of errors do you know?
* what techniques for finding bugs do you know?
* why do programmers create bugs?


.. seealso:: 

    - `Kristians Debugging Tutorial at PyData 2017 <>`__
    - Data from: `github.com/knkeniston/TwentyQuestions <https://github.com/knkeniston/TwentyQuestions/>`__
