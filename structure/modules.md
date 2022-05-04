
# Structuring Programs and Modules

## Programs
A program consists of multiple lines that are executed in one go.

Usually a program contains the following sections:

![input-processing-output](../images/ipo.png)

Of course, programs can grow a lot more complicated than that.


## What is a module?

Any Python file (ending .py) can be imported from another Python script. A single Python file is also called a module.

## Importing modules

To import from a module, its name (without .py) needs to be given in the import statement. Import statements can look like this:

    import fruit
    import fruit as f
    from fruit import fruit_prices
    from my_package.fruit import fruit_prices

It is strongly recommended to list the imported variables and functions explicitly instead of using the *import &#42;* syntax. This makes debugging a lot easier.

When importing, Python generates intermediate code files (in the *__pycache__* directory) that help to execute programs faster. They are managed automatically, and dont need to be updated.
