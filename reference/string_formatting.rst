String formatting
=================

Variables and strings can be combined, using **f-strings**. f-strings
contain placeholders with variable names and format characters. Here are
some examples:


.. code:: python3

   name = 'Roger'
   number = 42
   pi = 3.14159

   print(f'Hello {name}')
   print(f'Result: {number:6d}')
   print(f'{number:06d}')
   print(f'{name:>20} {name:20}')
   print(f'{pi:8.3f})

The winged brackets are placeholders for the parameters in the
``format`` function. Thy consist of two parts ``{a:b}``. Part ``a`` is a
variable name (or expression). The optional part ``b`` contains format
characters. Options include:

-  ``{var}`` – insert the variable only.
-  ``{var:xd}`` – an integer with x digits.
-  ``{var:<xd}`` – a left-formatted integer with x digits.
-  ``{var:0xd}`` – a left-formatted integer with x digits filled up with
   zeroes.
-  ``{:>5}`` – a right-aligned string of width 5.
-  ``{:6.2f}`` – a float number with 6 digits (2 after the dot).

Remark
~~~~~~

The older method ``.format()`` (prior to Python 3.6) is sometimes used
for string formatting:


.. code:: python3

   print('{:6.3f}/{:6.3f}'.format(a, b))
