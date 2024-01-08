
Running Code from a Terminal
============================

In this chapter, you find a recipe to run a Python program from a command line or terminal.
The recipe focuses on Windows users, because this is where the problem is  most prevalent.

Step 1: Create a project folder
-------------------------------

Create a new folder for the project.
In this exammple, name it ``hello``.

Step 2: Create a Python file
----------------------------

Open your favorite code editor and create a new file ``hello.py``.
Write a single line into it:

.. code:: python3

   print("hello world")

Store it in the new project folder ``hello``.


Step 3: Open a terminal
-----------------------

Start a new terminal session.

On Windows, search for **Anaconda Prompt** in the Start Menu.

In any case, you should see the text `(base)` at the beginning of the line with the prompt.
This means Anaconda is installed and the terminal is properly set up for it.

Step 4: Change directory
------------------------

Use the `cd <folder>` command to switch in the terminal to the new project directory.

On Windows, you can click into the address bar of the browser, copy the complete PATH to your project and paste it right after the `cd` command.

When you type `dir` or `ls`, you should see the contents of the folder.

Step 5: Run the program
-----------------------

In the same terminal, type:

::

    python hello.py

And you should se the message `hello world` appear.
