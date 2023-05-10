Lists
=====

A list is a Python data type representing a sequence of elements. You
can have lists of strings:


.. code:: python3

   names = ['Hannah', 'Emily', 'Madison', 'Ashley', 'Sarah']

and also lists of numbers:


.. code:: python3

   numbers = [25952, 23073, 19967, 17994, 17687]

Accessing elements of lists
---------------------------

Using square brackets, any element of a list and tuple can be accessed.
The first character has the index 0.


.. code:: python3

   print(names[0])    
   print(numbers[3])

Negative indices start counting from the last character.


.. code:: python3

   print(names[-1])

Creating lists from other lists:
--------------------------------

Lists can be sliced by applying square brackets in the same way as
strings.


.. code:: python3

   names = ['Hannah', 'Emily', 'Sarah', 'Maria']
   names[1:3]      
   names[0:2]      
   names[:3]
   names[-2:]

Copying a list
--------------

You can use slicing to create a copy:


.. code:: python3

   girls = names[:]

Adding elements to a list
-------------------------

Add a new element to the end of the list:


.. code:: python3

   names.append('Marilyn')

Removing elements from a list
-----------------------------

Remove an element at a given index:


.. code:: python3

   names.remove(3)

Remove the last element:


.. code:: python3

   names.pop()

Replacing elements of a list
----------------------------

You can replace individual elements of a list by using an index in an
assignment operation:


.. code:: python3

   names[4] = 'Jessica'

Sorting a list
--------------


.. code:: python3

   names.sort()

The ``itemgetter`` module allows you to sort lists by a specific column.
E.g. to sort names by the 3rd character:


.. code:: python3

   from operator import itemgetter

   cities.sort(key=itemgetter(2))

You can give a tuple of indices to sort first by one, then the other
column:


.. code:: python3

   cities.sort(key=itemgetter((1, 0)))

Counting elements
-----------------


.. code:: python3

   names = ['Hannah', 'Emily', 'Sarah', 'Emily', 'Maria']
   names.count('Emily')
