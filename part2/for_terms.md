# Definitions

## Loops with for

The `for` loop allows you to repeat one or more instructions. It requires a sequence of items that the loop iterates over. This can be e.g. a string. 

Later we will see how you can run `for` loops over other things e.g. a list, a tuple, a dictionary, a file or a function. Some examples:

    for char in 'ABCD':
        print(char)

    for i in range(3):
        print(i)

    for elem in [1,2,3,4]:
        print(elem)

## When to use for?

* When you want repeat an operation
# When you want to do something to all characters of a string.
* When you want to do something to all elements of a list.
* When you already know the number of iterations.

## Reserved words

The two words `for` and `in` are also called **reserved words**. They have a special meaning in Python, which means that you cannont call a variable `for` or `in`. There are 33 reserved words in Python 3.

You can see the complete list with the commands:

    import keyword
    keyword.kwlist

## Code blocks and indentation

The line with the `for` statement, a **code block** starts. A code block contains one or more line that belong to the `for` and are executed within the loop. Python recognizes this code block by **indentation**, meaning that each line starts with four extra spaces.

Indentation is a central element of Python syntax. Indentation must not be used for decorative purposes.

There are other Python commands that are also followed by code blocks. All of them end with a colon (`:`) at the end of the line.

### Code blocks in the IPython shell
Define code blocks by indenting extra lines:

    In [1] for i in range(3):
    ...     print(i)
    ...
    0
    1
    2
    In [2]
