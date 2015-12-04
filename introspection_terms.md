
# Definitions

Introspection is a feature of Python by which you can examine objects (including variables, functions, classes, modules) at runtime. 

## Exploring the namespace
In Python classes, functions, modules etc. have separate namespaces. A namespace is the set of attributes of an object. You can explore a namespace with `dir()`:

    print dir()
    import time
    print dir(time)

## Built-in help
You can get context-sensitive help to functions, methods and classes that utilize the triple-quoted comments:
import time
print help(time.asctime)


## Everything is an Object
One consequence of the dynamic typing is that Python can treat everything it manages technically in the same way. Everything is an object, meaning it has attributes. These attributes are objects themselves. Methods are simply attributes that can be called. 

## Each object has a name:

    print (x.__name__)

and a type:

    print (type(x))
