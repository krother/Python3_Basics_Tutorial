
## 6. Type conversions

Now we are going to combine strings with integer numbers.

    name = 'Emily Smith'
    born = _____
    ____ = '15'

    text = ____ + ' was born in the year ' + _____
    year = born + _____
    text
    year

Insert into the following items into the code, so that all statements are working: `age`, `int(age)`, name, `str(born)`, `2000`

#### Questions

* Can you leave `str(born)` and `int(age)` away?
* What do `str()` and `int()` do?

## Definitions

### Type conversions

If you have an integer number `i`, you can make a string out of it with `str(i)`:

    text = str(2000)

If you have a string `s`, you can make an integer out of it with `int(s)`:

    number = int("2000")

Both `int()` and `str()` change the type of the given data. They are therefore called **type conversions**.

### Functions

With `int()` and `str()`, you have just learned to know two **functions**. In Python, functions consist of a *name* followed by **parentheses**. They can have parameters, so that a function is used like:

    y = f(x)

Using a function is a regular Python statement (or part thereof). It is executed only once


## Exercises

### Exercise 6.1: Examine types

What is the result of the following statements?

     9 + 9

     9 + '9'

     '9' + '9'

### Exercise 6.2: Type conversions

Change the statements above by adding int() or str() to each of them, so that the result is 18 or '99', respectively.

### Exercise 6.3: A data record with types

| field      | value    | type |
|------------|----------|------|
| first name | Andrew   | string |
| last name  | O'Malley | string |
| gender     | M | string |
| year of birth | 2000  | integer |
| age | 15 | integer |

Write the values from each row of the table into string or integer variables, then combine them to a single one-line string.
