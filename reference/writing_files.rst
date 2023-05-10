Writing text files
==================

Opening a file for writing
--------------------------

Writing text to files is very similar to reading. One main difference is
that you need to add the ``'w'`` parameter for *writing*.


.. code:: python3

   f = open('my_file.txt','w')
   f.write(text)
   f.close()

Writing a list of strings
-------------------------

If your data is a list of strings, it can be written to a file in one
line of code. You only need to take care of adding line breaks at the
end of each line:


.. code:: python3

   lines = ['first line\n', 'second line\n']
   open('my_file.txt','w').writelines(lines)

Writing a table to a text file
------------------------------

A straightforward pattern to write multiple columns to a file uses a
``for`` loop to create lines with separators and newline characters:


.. code:: python3

   names = ['Emily', 'Bob', 'Charlie']
   ages = [23, 45, 67]

   f = open('my_file.txt', 'w')
   for name, age in zip(names, ages):
       line = "{};{}\n".format(name, age)
       f.write(line)
   f.close()

Like with reading, the ``csv`` and ``pandas`` offer more sophisticated
ways to write tables.

Appending to a file
-------------------

It is possible to append text to an existing file, too.


.. code:: python3

   f = open('my_file.txt','a')
   f.write('line appended at the end\n')
   f.close()

Closing a file after writing
----------------------------

When writing data, Python *buffers* the data and writes it to the disk
with a delay. The writing occurs after the file has been closed, when
Python ends or when the buffer runs full. By using ``close()`` you make
sure the data gets written.


.. code:: python3

   f.close()

Writing to a file with a Context Manager
----------------------------------------

The ``with`` statement is a **Context Manager** that takes care of
closing a file automatically:


.. code:: python3

   with open('my_file', 'w') as f:
       f.write('line of text\n')
