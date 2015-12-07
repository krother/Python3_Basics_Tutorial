
# Definitions

## The os module

Here, we will for the first time use a function that is not readily available in Python - it needs to be imported:

    import os

`os` is the name of a module that is automatically installed with Python. It is simply not kept in memory all the time. This is why we need to import it.

In this section of the tutorial, you will need just one function from the module. The function 
    
    y = os.listdir("x")

gives you a list of all files in the directory `x` and stores it in the variable `y`.

