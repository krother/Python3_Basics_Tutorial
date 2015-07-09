
# Structuring programs with functions, modules and packages

In Python, you can structure programs on four different levels: with functions, classes, modules and packages. Of these, classes are the most complicated to use. Therefore they are skipped in this tutorial.

## Functions

### What is a function?
A function is an autonomous sub-program with local variables, input and output, and its own namespace. 
In Python, a function definition must be followed by a code block:

    def calc_price(fruit,n):	
    '''Returns the price of fruits.'''
        if fruit=='banana':
            return 0.75 * n

    print(calc_price('banana',10))

### Optional parameters

Function parameters may have default values. In that case, they become optional. Do not use mutable types as default arguments!

    def calc_price(fruit, n=1): 
        ..

    print(calc_prices('banana'))
    print(calc_prices('banana',100))

### List and keyword parameters

You can add a list &#42;args for an unspecified number of extra parameters, or a dictionary &#42;&#42;kwargs for keyword parameters.

    def func(&#42;args, &#42;&#42;kwargs):
        print(args, kwargs)

    func(1, 2, a=3, b=4)

### Return values

A function may return values to the program part that called it. 

    return 0.75

Multiple values are returned as a tuple. 

    return 'banana', 0.75

In any case, the return statement ends the execution of a function.


## Modules

### What is a module?

Any Python file (ending .py) can be imported from another Python script. A single Python file is also called a module.

### Importing modules

To import from a module, its name (without .py) needs to be given in the import statement. Import statements can look like this:

    import fruit
    import fruit as f
    from fruit import fruit_prices
    from my_package.fruit import fruit_prices

It is strongly recommended to list the imported variables and functions explicitly instead of using the *import &#42;* syntax. This makes debugging a lot easier.

When importing, Python generates intermediate code files (in the *__pycache__* directory) that help to execute programs faster. They are managed automatically, and dont need to be updated. 

## Packages

### What is a package?

For big programs, it is useful to divide up the code among several directories. These are called packages. Technically, a package is a directory containing Python files. To import a package from outside, there needs to be a file *__init__.py* (it may be empty).

### Where does Python look for modules and packages?

When importing modules or packages, their directory needs to be in the Python search path.

Python looks for modules and packages in:

* The current directory.
* The site-packages folder (where Python is installed).
* In directories in the PYTHONPATH environment variable.

You can see all directories from within Python by checking the *sys.path* variable:

    import sys
    print sys.path


## Exercises

### Exercise 1

Join the right halves of sentences.

![functions exercise](exercises/functions.png)

### Exercise 2

Which `import` statements are correct?

- [ ] `import re`
- [ ] `import re.sub`
- [ ] `from re import sub`
- [ ] `from re import *`
- [ ] `from re.sub import *`

### Exercise 3

Where does Python look for modules to import?

- [ ] in the variable `sys.path`
- [ ] in the current working directory
- [ ] in the directory where the current module is
- [ ] in the `site-packages` folder
- [ ] in directories in the `PYTHONPATH` variable

### Exercise 4

Which statements about packages are true?

- [ ] a package is a directory with modules
- [ ] a package must contain a file `__init__.py`
- [ ] a package may contain no code
- [ ] a module may contain many packages

### Exercise 5

Which packages are installed by default?

- [ ] `os` - manipulating files and directories
- [ ] `time` - accessing date and time
- [ ] `csv` - read and write tables
- [ ] `numpy` - number crunching
- [ ] `pandas` - clever handling of tabular data
















