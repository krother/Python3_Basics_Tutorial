# Advantages of Object-oriented Programming

* Encapsulation: data and code stick together
* Code reuse: inherit and dont write all anew
* Maintenance: errors are easier to find/less frequent
* Structure: additional level of grouping things
* Consistency: People are used to think in objects (programmers too)
* Polymorphism: similar objects do different things
* Objects are good dimension for Unit testing

## Disadvantages: 

* Code is a little longer (for doing small tasks)
* Code is a little slower (when there are many instances)


## Abstract Superclasses
An abstract class can do nothing on its own, but it has some methods or attributes that subclasses can use. For instance, the Queue and Stack classes have some similar properties like managing an ordered set of items, having a push() and pop() method. A common superclass for the two could contain methods that do the same in both of them, like __init__(), __len__(), __str__() and maybe others.

Often, programmers use a superclass just to make sure that some methods exists, and leave them empty (see the example).

## Multiple Inheritance:
Python classes can inherit from multiple ancestors at the same time. Don't do this if you can avoid it. This can be useful in particular cases, but creates confusing cases when several ancestors have methods with the same name. Even experienced programmers should take this as a last option.
