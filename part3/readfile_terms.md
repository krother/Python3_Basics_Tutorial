
# Definitions

## Opening a file for reading

Text files can be accessed using the `open()` function. `open()` gives you a *file object* that you can use in a `for` loop:

    f = open('my_file.txt')
    for line in f:
        ...    

Alternatively, you can write both commands in one line:

    for line in open('my_file.txt')

### Reading a file to a string

You can read the entire content of a file to a single string:

    f = open('my_file.txt')
    text = f.read()


## Writing directory names in Python

When opening files, you often need to specify a directory name as well. You can use both full or relative directory names. 

On Windows, this is a bit more cumbersome, because you must replace the backslash `\` by a double backslash `\\` (because `\` is also used for escape sequences like `\n` and `\t`).

    f = open('..\\my_file.txt')
    f = open('C:\\python\\my_file.txt')


## Closing files

Closing files in Python is not mandatory but good practice.

    f.close()

