Cleaning Up
===========

Cleaning up code is an everyday activity of any prorammer.
Clean programs are shorter, easier to understand and easier to change.
The process of cleaning up is also called **refactoring**. 
More specifically, refactoring means **improving the structure of a program without
changing its functionality.**

In this chapter, you will learn basic techniques to refactor a program.


Exercise 1
----------

In :download:`connect_four.py` you find a working implementation
of a simple *“Connect Four”* game.
Writing such a program for the first time is a huge success!

Run the game and see how it works.


Exercise 2
----------

The first implementation often requires clean-up.
Read the code in :download:`connect_four.py`

Do you see any problems in the code?

Exercise 3
----------

Apply the following refactorings:

-  extract a variable
-  extract a loop
-  extract function
-  split a function
-  merge redundant blocks
-  introduce a state variable for the winning status
-  introduce a **main** block

After each refactoring, make sure the program still works.
