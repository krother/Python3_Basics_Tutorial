
# Dictionaries

Dictionaries are an unordered, associative array. They have a set of key/value pairs. They are very versatile data structures, but slower than lists. Dictionaries can be used easily as a hashtable.

## Creating dictionaries

    prices = {
            'banana':0.75,
        'apple':0.55,
        'orange':0.80
        }

## Accessing elements in dictionaries

By applying square brackets with a key inside, the values of a dictionary can be requested. Valid types for keys are strings, integers, floats, and tuples.

    print prices['banana']  # 0.75
    print prices['kiwi']    # KeyError!

## Looping over a dictionary:

You can access the keys of a dictionary in a for loop. However, their order is not guaranteed, then.

    for fruit in prices:
        print fruit

## Dictionary functions

There is a number of functions that can be used on every dictionary:

#### Checking whether a key exists:

    prices.has_key('apple')

#### Retrieving values in a fail-safe way:

    prices.get('banana')
    prices.get('kiwi')

#### Setting values only if they dont exist yet:

    prices.setdefault('kiwi', 0.99)
    prices.setdefault('banana', 0.99)
    # for 'banana', nothing happens

#### Getting all keys / values:

    print prices.keys()
    print prices.values()
    print prices.items()

