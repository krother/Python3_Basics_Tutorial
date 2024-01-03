Spiral
======

**Write a program, that draws a spiral:**

.. figure:: spiral1.svg
   :alt: spiral

When your program draws a spiral with at least 3 loops, you have
mastered this challenge.

What you can practise in this coding challenge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  loops
-  The **turtle** module in Python

Hints
~~~~~

-  It is sufficient to draw the spiral as a series of short lines
-  Where is it easier to start (inside or outside)?
-  Both the Python modules ``Pillow`` and ``turtle`` are up to the task

Getting started
~~~~~~~~~~~~~~~

If you have no idea where to start, try the following Python script:

.. code:: python3

   from turtle import forward, left

   forward(50)
   left(90)
   forward(50)

Extra Challenge
~~~~~~~~~~~~~~~

-  the line width grows thicker from the inside to the outside
-  there is a color gradient along the spiral
-  draw the **Fibonacci spiral** instead

.. figure:: spiral2.svg
   :alt: Spiral with width and color
