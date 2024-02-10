Rock-Paper-Scissors
===================

|image0|

`image by Enzoklop, CC BY-SA
3.0 <https://commons.wikimedia.org/w/index.php?curid=27958795>`__


In this chapter you will:
-------------------------

======= ====================================
area    topic
======= ====================================
🚀      write a *rock-paper-scissors* game
⚙       use the conditional statement ``if``
⚙       use comparison operators
💡      use the data type ``bool``
🔀      use a state variable
🐞      recognize indentation errors
======= ====================================

An important structural element in program is *making decisions*.
In Python, the instruction ``if`` 
decides which instruction to execute next.


Exercise 1: Decision
--------------------

With the instruction ``if``, you can make a decision inside your program. 
Test the following program with different inputs:

.. code:: python3

   player = input("Please enter R, P or S (for [R]ock, [P]aper and [S]cissors) ")
   computer = "P"

   if player == computer:
       print("it's a draw")


Exercise 2: Alternative decisions
---------------------------------

Insert the words ``elif``, ``else`` and ``if`` into the gaps in the code
so that it runs:

.. code:: python3

   import random

   player = input("Please enter R, P or S (for [R]ock, [P]aper and [S]cissors) ")
   computer = random.choice('RPS')

   ___ player == 'R' and computer == 'P':
       print("Computer wins")
   ___ player == 'R' and computer == 'S':
       print("Player wins")
   ___:
       print("it's a draw")


Exercise 3: Paper
-----------------

Extend the program, so that it also works if the player chooses *paper*.


Exercise 4: Debugging
---------------------

Fix one bug in each ``if``-statement:

.. code:: python3


   elif player.upper() not in 'RPS':
       print('Invalid input. Please enter R,P or S.')

   elif player == computer
       print('You chose the same as I did')

   if player = 'S':
       print('You chose "scissors".')

   else:
   print('You chose something else than "scissors"')


Exercise 5: Expressions
-----------------------

Which comparisons in the following ``if`` statements result in ``True``:

.. code:: python3

   a = 3
   b = 4
   c = 7

   if a + b < c:
       print(True)

   if a + b == 5 + 2:
       print(True)

   if a * b == 12 and b * c == 28:
       print(True)

   if a + b * c >= 28:
       print(True)

   if a + b == "7":
       print(True)


Exercise 6: State variables
---------------------------

The following program saves the result of a comparison
in a variable of the data type ``bool``.
Complete the code:

.. code:: python3

   player_wins = (
                  (player == "R" and computer == "S") or
                  (player == "P" and ___) or
                  (___)
                 )

   if player_wins:
       print('You won!')


Exercise 7: Nested if statements
--------------------------------

Complete the program, so that it covers all possible situations:

.. code:: python3

   winner = 'draw'

   if player == "S":
       if computer == "P":
           winner = "player"
       elif computer == "T":
           winner = "computer"

   elif player == "P":
       ___

   print("The winner is:", winner)

.. hint::

   A *nested if* is an if inside another if block.


Exercise 8: Rock-Paper-Scissors
-------------------------------

Complete the Rock-Paper-Scissors game.

Optional goals:
~~~~~~~~~~~~~~~

-  take draws into account as a possibility
-  inputs should be valid in upper and lower case
-  use a single ``if..elif..else`` block
-  extend the game by `lizard and Spock <https://en.wikipedia.org/wiki/Rock_paper_scissors#Additional_weapons>`__
-  use ``bool`` variables, so that only one or two ``if`` statements
   without ``elif`` or ``else``) remain

Reflection Questions
--------------------

* in which order do the parts of an ``if`` statement have to be?
* which parts of an ``if`` statement are optional?
* what is indentation?
* which *comparison operators* do you know so far?


.. |image0| image:: rock_paper_scissors.svg
