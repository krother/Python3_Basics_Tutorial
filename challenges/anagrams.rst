Anagrams
========

**🎯 Check whether two words are anagrams of each other.**

For example, the string:

::

   players

has the anagram (permutations of characters):

::

   parsley

Write a function `anagram()` that satisfies the following checks:

.. code:: python3

   assert anagram("players", "parsley") is True
   assert anagram("hello", "world") is False

Hints
-----

- consider sorting the characters
- consider the `set()` data type
- consider `collections.Counter`
- look up the function `itertools.permutations()`.

Extra challenges
----------------

-  Look for anagrams in the `SOWPODS word list <https://www.freescrabbledictionary.com/sowpods/download/sowpods.txt>`__ .
-  Implement an algorithm to generate all possible anagrams. Inform yourself about **dynamic programming**.
-  what is the time complexity of your implementation?

*Translated with* `www.DeepL.com <https://www.DeepL.com/Translator>`__
