Greatest Common Denominator
===========================

**🎯 Implement the** `Euclidean
Algorithm <https://en.wikipedia.org/wiki/Euclidean_algorithm>`__ **to
determine the greatest common denominator of two integers.**

Pseudocode
----------

1. you have two integer numbers a and b
2. copy the value of b
3. set b to the modulo of a and b
4. set a to the copy of b
5. if b is not zero, go back to step 2.
6. a is the greatest common denominator of a and b

Tests
-----

Use the following code to test your function:

.. code:: python3

   assert gcd(6, 3) == 3
   assert gcd(12, 8) == 4
   assert gcd(42, 12) == 6


*Translated with* `www.DeepL.com <https://www.DeepL.com/Translator>`__
