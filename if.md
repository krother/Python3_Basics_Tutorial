
# Control flow statements

Control flow means controlling, which instruction is handled next. In this tutorial, we cover three of Pythons control flow statements: `for`, `if` and `while`.

# Definitions

## Conditional statements with `if`

if statements are used to implement decisions and branching in the program. They must contain an `if` block, and zero or more `elif`'s and an optional `else` block:

    if fruit == 'apple':
        price = 0.55
    elif fruit == 'banana':
        price = 0.75
    elif fruit == 'orange':	
        price = 0.80
    else:
        print 'we dont have %s'%(fruit)

## Boolean value of variables

Each variable can be interpreted as a boolean (`True`/`False`) value. All values are treated as `True`, except for:

    False
    0
    []
    ''
    {}
    set()
    None

## Comparison operators
An `if` expression may contain comparison operators like:

    a == b
    a != b
    a < b
    a > b
    a <= b
    a >= b
    a in b  # when b is a list

Multiple expressions can be combined with boolean logic:

    a or b
    a and b
    not a
    (a or b) and (c or d)

## Code blocks

After an `for` or `if` statement, all indented commands are treated as a code block, and are executed in the context of the condition.

The next unindented command is executed in any case.

# Exercises

## Exercise 1

Which of these `if` statements are syntactically correct?

- [ ] `if a and b:`
- [ ] `if len(s) == 23:`
- [ ] `if a but not b < 3:`
- [ ] `if a ** 2 >= 49:`
- [ ] `if a != 3`
- [ ] `if (a and b) or (c and d):`
