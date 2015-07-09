# 10. Loops

## Example

    characters = "ABCDE"
    for char in characters:
        print(char)

## Definitions

### Loops with for

The `for` loop allows you to repeat one or more instructions. It requires a sequence of items that the loop iterates over. This can be a list, a tuple, a string, a dictionary or any iterator-like object (e.g. a file). Some examples:

    for i in range(3):
        print(i)

    for char in 'ABCD':
        print(char)

    for elem in [1,2,3,4]:
        print(elem)

### When to use for?

* When you want repeat an operation
# When you want to do something to all characters of a string.
* When you want to do something to all elements of a list.
* When you already know the number of iterations.

### Reserved words

The two words `for` and `in` are also called **reserved words**. They have a special meaning in Python, which means that you cannont call a variable `for` or `in`. There are about 30 reserved words in Python.

### Code blocks and indentation

The line with the `for` statement, a **code block** starts. A code block contains one or more line that belong to the `for` and are executed within the loop. Python recognizes this code block by **indentation**, meaning that each line starts with four extra spaces.

Indentation is a central element of Python syntax. Indentation must not be used for decorative purposes.

There are other Python commands that are also followed by code blocks. All of them end with a colon (`:`) at the end of the line.

#### Code blocks in the IPython shell
Define code blocks by indenting extra lines:

    In [1] for i in range(3):
    ...     print(i)
    ...
    0
    1
    2
    In [2]

## Exercises

### Exercise 10.1

What does the following program do:

    text = "" 
    characters = "ABCDE"
    for char in characters:
        text = char + text
    print(text)

### Exercise 10.2

Write a for loop that creates the following output

    000
    111
    222
    333
    444
    555
    666
    777
    888
    999

### Exercise 10.3

Write a for loop that creates the following string as a variable

    000111222333444555666777888999

### Exercise 10.4

Write a for loop that calculates the number of characters in "Emily Smith".

### Exercise 10.5

Write a for loop that creates the following output

    1
    3
    6
    10
    15
    21
    28

### Exercise 10.6

Write a for loop that creates the following string

    "1 4 9 16 25 36 49 64 81 "

### Exercise 10.7

Add a single line at the end of the program, so that it creates the following string:

    "1 4 9 16 25 36 49 64 81"


