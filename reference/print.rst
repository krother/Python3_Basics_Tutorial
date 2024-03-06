Writing to the Screen
=====================

The command ``print()`` Writes tex output to the screen. It accepts one
or more arguments in parentheses - all things that will be printed. You
can print both strings and integer numbers. You can also provide
variables as arguments to ``print()``.

We need ``print`` because typing a variable name in a Python program
does not give you any visible output.

The Python ``print`` function is very versatile and accepts many
combinations of strings, numbers, function calls, and arithmetic
operations separated by commas.

Examples for print statements:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python3

   print('Hello World\n')
   print(3 + 4)
   print(3.4)

   print("""Text that 
   stretches over 
   multiple lines.
   """)

   print('number', 77)

   a = "7"
   print(a * 7)
   print(int(a) * 7)
   print("Hello", end=" ")
   print("World")
