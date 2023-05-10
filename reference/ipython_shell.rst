The IPython Shell
=================

The IPython shell allows you to enter Python commands one by one and
executes them promptly. The IPython shell is a luxury version of the
simpler Python shell. It is also called *interactive mode* or
*interactive Python command line*.

You can use any Python command from the *IPython Shell*:


.. code:: python3

   In [1]: 1 + 1
   Out[1]: 2
   In [2]: 4 * 16
   Out[2]: 64
   In [3]:

Results of each command are automatically printed to the screen.

How to leave the IPython shell?
-------------------------------

-  You can leave the command line by Ctrl-z (Windows) or Ctrl-d (Linux).
-  If a program seems to be stuck, you can interrupt the shell with
   Ctrl-c.

Magic Methods
-------------

The IPython shell has a number of special commands or **Magic Methods**.
Here are the most common ones:

============== =========================================
command        description
============== =========================================
``%run``       execute a program
``%paste``     paste and execute code from the clipboard
``%hist``      show recently entered commands
``ls``         show files in the current directory
``pwd``        print the current working directory
``cd <dir>``   change the working directory to ``<dir>``
``!<command>`` execute ``<command>`` on the bash
============== =========================================
