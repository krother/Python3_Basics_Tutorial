Look up Prices
==============

In this chapter you will:
-------------------------

======= ====================================
area    topic
======= ====================================
🚀      write a better receipt assistant
⚙       define a dictionary
⚙       look up values of a dictionary
🔀      iterate through a list of dictionary keys
🔀      use lists as dictionary values
🐞      fix errors in dictionary definitions
🐞      fix index errors
======= ====================================

Exercise 1: Look up
-------------------

Consider we would like to look up shopping prices.
In this chapter, we will use a **dictionary**,
a data structure that is good for looking up items.

Execute the following code:

.. code:: python3

   prices = {
      "apple": 0.50,
      "banana": 1.00,
      "orange": 1.50,
      "cherries": 3.00,
   }
   print(prices["banana"])

How does the dictionary differ from a list?


Exercise 2: Explore
-------------------

Find out what each of the expressions does to the dictionary in the center.

.. figure:: dicts.png
   :alt: dict exercise


Exercise 3: Look up
-------------------

Now consider having the list of items in ``fruit``.
You would like to calculate the total price.
For that, the list and dictionary need to work together.

Sort the lines and indent them properly:

   print(total)
   total += prices[item]
   bought = ["banana", "banana", "cherries", "apple", "apple", "banana"]
   for item in bought:
   total = 0
   prices = {
      "apple": 0.50,
      "banana": 1.00,
      "orange": 1.50,
      "cherries": 3.00,
   }

Exercise 4: Receipt assitant 2.0
--------------------------------

Improve the receipt assistant from the previous chapter
so that it uses a dictionary of prices.


Exercise 5: Traveler
--------------------

The following program allows you to travel from one city to the next.
Unfortunately, it contains **five bugs**. Find and fix them.

.. code:: python3

   cities = {
       "New York": ["Tokyo", "Delhi", "London"],
       "Poznan": ["London", "Berlin"],
       "London": ["New York", "Poznan"]
       "Berlin": ["Tokyo", "Poznan"],
       "Tokyo": ["New York" "Berlin"],
       "Delhi": ["Katmandu"]
       }

   location = "Berlin"
   print "\nYour task: fly to Katmandu\n"

   while location in cities and location == 'Katmandu':
       print(f"You are in {location}")

   print("There are flights to ", cities["location"])
   location = input("Where would you like to travel?")

   print("You have reached your destination")


Reflection Questions
--------------------

-  How can you create a dictionary?
-  What data types can you use as keys of a dictionary?
-  What data types can you use as values of a dictionary?
-  How can you modify values in a dictionary?
-  Is it possible to run a for loop over a dictionary?
