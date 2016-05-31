
## Comments

In Python, single lines can be commented by the hash symbol (`#`):

    # this is a comment.
    print(a + b)  # adding the variables

Also, multi-line comments can be enclosed by triple quotes:

    '''
    This is a longer description
    that stretches over multiple lines.
    '''

#### Hint
The triple quoted comments can be used to generate documentation automatically. 



### Exercise 8.2

Which lines are commented?

- [ ] `"""This is a comment"""`
- [ ] `# This is a comment`
- [ ] `// This is a comment`
- [ ] `<!-- This is a comment !-->`
- [ ] `'''This is a comment'''`



### Length of strings

Is returned as an integer by the `len()` function.

    s = 'Manipulating Strings '
    print(len(s)


  len()
  dict
  if
  Kommentare
  escape characters
  Formatstrings
  math
  open()
  TRANSFER: Matrix mutable/immutable, simple/composed
  sum()
  sorted()
  import
  pip
  Bücher und Webseiten
  Eingabe-Verarbeitung-Ausgabe
  Copy-Paste-Programmierung
  Vom Skript zur Software
  Fehlerbehebung

# Aufgabe:

1. Datei mit Babynamen laden
2. ersten Buchstaben ausgeben
3. Gesamte Geburten für 1 Buchstaben
4. Gesamte Geburten für alle Buchstaben einzelnt
5. Ausgabe als Tabelle auf dem Bildschirm
7. Alle Jahrgänge laden
8. Tabelle Excel exportieren
9. Timeline plotten


Creating plots
The Matplotlib library contains a wide range of possibilities for creating graphs. See the 'gallery' link on http://matplotlib.sourceforge.net for examples. It needs to be installed separately.
from pylab import *
Number crunching
Numpy is a library that allows operating on arrays and matrices. It needs to be installed separately. See: http://numpy.scipy.org
import numpya = numpy.array( [1,2,3,4,5,6] )print a+10, a*a
Image manipulation
The Python Imaging Library PIL is a powerful tool for working with images (changing formats, resizing, cutting, drawing). It needs to be installed separately. See http://www.pythonware.com/products/pil .


# Review Questions

TODO: sort basic/advanced questions apart
* is it equivalent to initialize a variable at the beginning of the program or inside a loop? (see average.py for an example)
* Name a situation in which you would prefer a programming language other than Python?
* How to write a program that prints all file names in a folder?
* What is an object and what is a class? Describe the difference?

How can you swap the values of two variables?
How can you create a dictionary with some values inside?
How do the methods get(), has_key() and keys() of a dictionary differ?
How can you retrieve values from a dictionary when you do not know whether their keys exist?
How can you set values in a dictionary?
What is a list comprehension?
Is it possible to create a for loop over a dictionary?
How to sort values from a dictionary?
What is the dir(object) built-in function good for?
What does the getattr(object,name) built-in function return?
How can i execute a string containing Python code created by a Python program?
What can you do to make your programs run faster?
What can i use to calculate with numbers? Write down at least 5 python commands.
What can i do to manipulate strings? Write down at least 5 python commands.
What can i do with lists? Write down at least 5 python commands.
What can i do with dictionaries? Write down at least 5 python commands.

How can you:
Swap the values of two variables (Python Cookbook 1.2)
Create a dictionary (Python Cookbook 1.3)
Retrieve values from a dictionary (Python Cookbook 1.4)
Set values in a dictionary (Python Cookbook 1.5)
Loop through a list I (Python Cookbook 1.14)
Loop through a list II (Python Cookbook 1.15)
Loop through a text file (Python Cookbook 4.2).
Sort values from a dictionary (Python Cookbook 2.2)
Sorting list of objects by an attribute (Python Cookbook 2.8)
String handling (Python Cookbook 3.2-3.11)
Test if a string can be converted to an integer (Python Cookbook 3.13)
Write a text file (Python Cookbook 4.3)
Replace text in a file (Python Cookbook 4.4)

You have an integer variable a, and four different functions that should be called depending on the value of a. How would you implement this?
What does the assert statement do?
What kinds of operations should be wrapped in a try.. except clause.
How to create an exception on purpose?
Write two different ways to calculate the numbers from 1 to 10.
Write two different ways to call string.upper for each element of a list.
What different kinds of arguments can a function definition contain?
Which data types as function arguments are mutable, which are immutable?
For how long does a local variable defined in a function exist?
What is a function variable good for?
What are rules for good style of functions?
When a module is importet by three other modules in one program, how often is its initialization code run?
Name two different kinds of import statements.
What is a package?
Where does Python look for module files available for import?

Objects
An object is a container for data plus code. Name three advantages of writing programs with objects.
What is a class?
What is an instance?
How does a constructor method look like?
What are class attributes, what instance attributes?
Explain how inheritance works using the classes 'Plant', 'Vegetable', 'Carrot' and 'Cactus' and the methods 'grow()', 'hurt()' or 'eat()'?
Data types and structures
What kinds of values can the basic data types (boolean, integer, float and string) take?
What is a type cast and how is it written in Python?
What is the difference between a tuple and a list?
Which values of these data types are equivalent to None?
Which values of these data types are equal to a boolean True?
Enumerate five useful things that you can do with lists.
How to make a copy of an entire list?
How to loop through all elements of a dictionary?
How to check whether a dictionary has a certain key?
What data types work as keys of a dictionary?
What is the difference between a stack and a queue?
How many leafs has a binary tree with 7 nodes?
Give an example of a graph.
Operations
What is a floor division? How is it used in Python?
Where to look for the sine, cosine and square root functions?
What do programmers need to take care of when doing divisions?
What needs to be done before using the arithmetic operators (+, -, *, /) on Python objects?
Give an expression that checks whether a number is odd or even.
Does the arithmetic (+, -, *, /) or the AND operator have the higher priority?
What does the expression x<7 AND „small“ OR „big“ return?
Is an expression always evaluated completely?
How can you check whether a number variable is between two values?
How to cut off the last two characters of a string?
How to replace the letter A with B in a string?
How to make a list of string variables from a tab-separated string?
How to find out if a string starts with a decimal number?
Enumerate some elements of the regular expression syntax.
Are string functions or regular expressions faster?
Give a line of code that writes a list of strings to a file.
What parameters does the format string „%i str: %s %4.3f“ expect?
How to read text from the keyboard?
What do the escape characters \t and \n stand for?
Propose three different ways to write data to a file.

Where in your programs should you put triple-quoted documentation strings?
Which method is called if you convert an object to a string?
What do you see when reading the __doc__ string of a function, a module or an object?

What programs can you use to edit Python programs comfortably?

Name alternative Python interpreter(s)

What is a profiler?

What does EpyDoc do?

Name one thing you can do using a debugger, like pdb.

What is an object and what is a class? Describe the difference?