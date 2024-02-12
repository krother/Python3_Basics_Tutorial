Connect Four
============

Cleaning up code is an everyday activity of any prorammer.
Clean programs are shorter, easier to understand and easier to change.
The process of cleaning up is also called **refactoring**. 
More specifically, refactoring means **improving the structure of a program without
changing its functionality.**

In this chapter you will:
-------------------------

==== ==============================================
area topic
==== ==============================================
🚀   clean up a connect four game
🔧   read code
🔧   apply refactoring: extract a function
🔧   apply refactoring: extract a loop
🐞   remove redundant code
==== ==============================================

Exercise 1
----------

In :download:`connect_four.py` you find a working implementation
of a simple *“Connect Four”* game.
Writing such a program for the first time is a huge success!

Run the game and see how it works.


Exercise 2: Code review
-----------------------

The first implementation often requires clean-up.
Read the code in :download:`connect_four.py`

Do you see any problems in the code?


Exercise 3: Extract a function
------------------------------

In the code, there is a paragraph commented with *"print the game board*.
This code paragraph has a well-defined functionality.
Move it into a separate function.

Define a function at the beginning of the file:

.. code:: python3

    def print_board(board):
        ...

Move the code paragraph into that function.
Add a function call where you took the code from:

.. code:: python3

   while True:
       
       print_board(board):

   # first player moves
   ...

Run the game and make sure it still works.


Exercise 4: Redundant code
--------------------------

The code for the ``print_board()`` function 
appears a second time further below.

Replace the code by the same function call.

Because you already defined the function,
you can use it multiple times.
Your program should become shorter by a few lines.

Run the game and make sure it still works.

Exercise 5: A function with a parameter
---------------------------------------

The next paragraph from *"first player moves"* to *"end: player moves"*
can also be moved to a function.
This time, we introduce an extra function parameter: the symbol for the player.

Create a new function with the definition:

.. code:: python3

   def player_move(board, symbol):
       ...

Replace the ``"X"`` in the code by the new variable ``symbol``.
Use the function call:

.. code:: python3

   player_move(board, "X")

Run the game and make sure it still works.

Then, see if there is a similar code paragraph that you could replace by a function call.


Exercise 6: More functions
--------------------------

See if there are any other redundant blocks of code.
Move them into functions as well.

Then, run the game and make sure it still works.


Exercise 7: Extract a loop
--------------------------

Consider the following section of the code:

.. code:: python3

    if board[0][x - 1] == ".":
        y = 0
    if board[1][x - 1] == ".":
        y = 1
    if board[2][x - 1] == ".":
        y = 2
    if board[3][x - 1] == ".":
        y = 3
    if board[4][x - 1] == ".":
        y = 4

Here, there is redundant code on a smaller scale.
Each pair of lines differs only by a single number.
This code can be made shorter by using a ``for`` loop
that counts from 0 to 4.

What needs to be inserted into the two gaps?

.. code:: python3

   for i in range(5):
       if board[___][x - 1] == ".":
           y = ___

Run the game and make sure it still works.


The Code
--------

Here is the complete (unclean) code:

.. literalinclude:: connect_four.py
