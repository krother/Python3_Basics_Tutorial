
# Dictionaries

## Exercise 1: Explore

Find out what each of the expressions does to the dictionary in the center.

![dict exercise](dicts.png)

----

## Exercise 2: Commands

Define a dictionary:

    d = {
         'cat':'Katze',
         'dog':'Hund',
         'fish':'Fisch'
    }

Then run the following commands and find out what they result in:

    print(d['fish'])
    
    print('Hund' in d)

    print(list(d.keys()))

    print(d.get('Katze', 'unknown'))

    d.setdefault('cat', 'Stubentiger')
    print(d['cat'])

----

## Exercise 3

The following program allows you to travel from one city to the next.
Unfortunately, it contains **three bugs**. Find and fix them.

    cities = {
        "New York": ["Tokyo", "Paris", "London"],
        "Poznan": ["London", "Berlin"],
        "London": ["New York", "Poznan"]
        "Berlin": ["Tokyo", "Poznan"],
        "Tokyo": ["New York", "Berlin"],
        "Paris": ["Katmandu"]
        }
    
    location = "Paris"
    
    print "\nYour task: fly to Katmandu\n"
    
    while location in cities and location == 'Katmandu':
        print(f"You are in {location}")
    
    print("There are flights to ", cities[location])
    location = input("Where would you like to travel?")

    print("You have reached your destination")
    
----

## Reflection Questions

* How can you create a dictionary?
* How can you modify values in a dictionary?
* Is it possible to run a for loop over a dictionary?
