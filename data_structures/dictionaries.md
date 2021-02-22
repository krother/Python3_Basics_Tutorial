
# Dictionaries

## Exercise 1

Find out what each of the expressions does to the dictionary in the center.

![dict exercise](../images/dicts.png)


## Exercise 2

What do the following commands produce?

    d = {1:'A', 'B':1, 'A':True}
    print(d['A'])

- `False`
- `"B"`
- `True`
- `1`

## Exercise 3

What do these commands produce?

    d = {1:'A', 'B':1, 'A':True}
    print(d.has_key('B'))

- `1`
- `True`
- `"B"`
- `False`

## Exercise 4

What do these commands produce?

    d = {1:'A', 'B':1, 'A':True}
    print(d.values())

- `True`
- `['A', 1, True]`
- `3`
- `[1, 'B', 'A']`

## Exercise 5

What do these commands produce?

    d = {1:'A', 'B':1, 'A':True}
    print(d.keys())

- `[1, 'B', 'A']`
- `['A', 'B', 1]`
- `[1, 'A', 'B']`
- `The order may vary`


## Exercise 6

What do these commands produce?

    d = {1:'A', 'B':1, 'A':True}
    print(d['C'])

- `None`
- `'C'`
- `an Error`
- `False`


## Exercise 7

What do these commands produce?

    d = {1:'A', 'B':1, 'A':True}
    d.setdefault('C', 3)
    print(d['C'])

- `3`
- `'C'`
- `None`
- `an Error`
