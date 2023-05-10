Numbers
=======

Integer numbers
---------------

Numerical values without decimal places are called **integers** or
**ints**. In Python, integers are a predefined **data type**.


.. code:: python3

   a = 42

Floating-point numbers
----------------------

Numbers with decimal places are called **floating-point numbers** or
**floats**.


.. code:: python3

   b = 42.0
   pi = 3.14159

Arithmetical Operators
----------------------

The arithmetical symbols like ``+ - * /`` connecting two numbers are
called **operators**. In addition to the standard arithmetics a few
other operators are available:


.. code:: python3

   a = 7
   b = 4
   c = a - b      
   d = a * b      
   e = a / b      
   f = a % b      # modulo, 3
   g = a ** 2     # 49   
   h = 7.0 // b   # floor division, 1.0

If you perform arithmetics with integer numbers, the result is also an
integer. If one of the numbers is a float, the result will also be a
float. When you perform a division, the result is always a
floating-point number.

Rounding and binary representation
----------------------------------

Occasionally, seemingly simple floating-point calculations will result
in strange results, e.g. instead of ``0.3`` you might see:


.. code:: python3

   >>> 0.1 + 0.2
   0.30000000000000004

This is related to the underlying binary representation of
floating-point numbers. The precision of floats is by default 16 digits,
which is enough for most applications (be aware that it might not, if
you are doing astrophysics or other high-precision calculations).

(This happens in all programming languages that use floats with limited
precision, but they might round the floats automatically.)
