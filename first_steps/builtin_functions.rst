Substitution Cipher
===================

In this chapter you learn:
--------------------------

==== ==============================================
area topic
==== ==============================================
🚀   encrypt text with a substitution cipher
⚙    convert strings to lists and back
⚙    use a random seed
💡   use the ``random`` module
💡   use the ``string`` module
💡   use the ``zip`` function
🔀   use the ``dict(zip())`` pattern
🐞   fix IndexErrors
==== ==============================================

Exercise 1: Random string
-------------------------

The following code creates a random chiffre that we will use for encryption.
Insert ``alphabet``, ``chars``, ``join`` and ``random`` into the code:

.. code:: python3

   import random

   alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

   ___ = list(___)
   ___.shuffle(chars)
   chiffre = "".___(chars)
   print(chiffre)

Run the program a couple of times.


Exercise 2: Random seed
-----------------------

Add the following line after the import:

.. code:: python3

   random.seed(77)

Run the program a couple of times.
What changes?

Also try running the program with different numbers.


Exercise 3: Chiffre indices
---------------------------

Output each character from the chiffre and its index 
Simplify the following code using the function ``enumerate()``:

.. code:: python3

   i = 0
   for char in chiffre:
       print(i, char)
       i += 1


Exercise 4: Lookup dictionary
-----------------------------

Create a dictionary that maps unencrypted to encrypted characters:

.. code:: python3

   lookup = {}
   i = 0
   while i < len(alphabet):
       char = alphabet[i]
       lookup[char] = chiffre[i]
       i += 1
   print(lookup)

Execute the program slowly on paper to make sure you understand the index operations.

Exercise 5: Zip
---------------

Use the following code to make the program above simpler:

.. code:: python3

   for char, chif in zip(alphabet, chiffre)
       print(char, chif)

Once you understand what happens, also try:

.. code:: python3

   lookup = dict(zip(alphabet, chiffer))


Exercise 6: Encrypt
-------------------

Use the lookup dictionary to encrypt a message.
Use the following lines as a starting point:

.. code:: python3

   message = ...
   result = ""

   for char in message:
       result += ...
-
Exercise 7: Debugging
---------------------

What happens when you enter lowercase letters or special characters in the message?

Try the expression:

.. code:: python3

   print(lookup.get(";", "X"))

Fix the problem. 


Exercise 7: Decrypt
-------------------

Decrypt a message when all you know is the encrypted message and the random seed.


Reflection Questions
--------------------

- what does the ``enumerate()`` function do?
- what does the ``zip()`` function do?
- is a substitution cipher rather safe or unsafe?
- what is **symmetric encryption**?

.. seealso::

   **Further Reading**

   - `Kerckhoffs Principle <https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle>`__