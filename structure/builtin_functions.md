
# Shortcuts

Python 3.11 has 75 builtin functions.
To start writing useful programs, knowing about 25 of them is sufficient.
Here you find a few exercises where you use builtin functions to make code shorter.

## Exercise 1

Simplify the following code using the function `sum()`:

    counts = [356, 412, 127, 8, 32]

    total = 0
    for number in data:
        total = total + number
    print(total)

## Exercise 2

Simplify the following code using the function `range()`:

    i = 0
    while i < 10:
        print(i * '*')
        i += 1

## Exercise 3

Simplify the following code using the function `zip()`:

    names = ['Lilly', 'Lily', 'Leila', 'Lilja', 'Lillie']
    counts = [356, 412, 127, 8, 32]

    table = []
    i = 0
    while i < len(names):
        row = (names[i], counts[i])
        table.append(row)
        i += 1
    print(table)

## Exercise 4

Simplify the following code using the function `enumerate()`:

    names = ['Lilly', 'Lily', 'Leila', 'Lilja', 'Lillie']

    i = 0
    for name in names:
        print(i, name)
        i += 1

## Exercise 5

Use `list(range())` to create the following lists:

    [4, 7, 9, 12]
    
    [10, 20, 30, 40, 50]
    
    [33, 32, 31, 30]
    

## Exercise 6

On which data types does the `len()` function work?

* lists
* dictionaries
* strings
* floats
* sets
