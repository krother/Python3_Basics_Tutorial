
Introspection and Namespaces
Introspection is a feature of Python by which you can examine objects (including variables, functions, classes, modules) at runtime. 
Everything is an Object
One consequence of the dynamic typing is that Python can treat everything it manages technically in the same way. Everything is an object, meaning it has attributes. These attributes are objects themselves. Methods are simply attributes that can be called. 
Each object has a name:
print x.__name__
and a type:
print type(x)
Built-in help
You can get context-sensitive help to functions, methods and classes that utilize the triple-quoted comments:
import time
print help(time.asctime)
Namespaces
In Python classes, functions, modules etc. have separate namespaces. A namespace is the set of attributes of an object. You can explore a namespace with dir():
print dir()
import time
print dir(time)
Namespaces are nested
When using a name, Python first uses the local namespace (e.g. of a function/method), then in the class, module, package, and finally in the global namespace.


Python library modules
The CSV module
The csv module reads tables from text files.
import csv
reader = csv.reader(open('my_file.csv'))
for row in reader:
    print row
Similarly, tables can be written to files:
write = csv.writer(open('my_file.csv','w'))
write.writerow(table)
Options of CSV file readers/writers
Both CSV readers and writers can handle a lot of different formats. Options you can change include:
delimiter : the symbol separating columns.
Quotechar : the symbol used to quote strings.
Lineterminator : the symbol at the end of lines.
reader = csv.reader(open('my_file.csv'),  delimiter='\t', quotechar='”')
Getting time and date
The time module offers functions for getting the current time and date.
import time
s = time.asctime()   # as string
i = time.time()      # as float
Accessing web pages
The HTML code of web pages and downloadable files from the web can be accessed in a similar way as reading files:
import urllib2
url = 'http://www.google.com'
page = urllib.urlopen(url)print page.read()



Regular Expressions
Regular expressions allow to perform string search & replace operations using patterns.
Searching
import re
text = 'all ways lead to Rome'
Search for a pattern in a string:
re.search('R...\s', text)
Find all words:
re.findall('\s(.o)', text)
Replacing
re.sub('R[meo]+','London', text)
How to find the right pattern for your problem:
Finding the right RegEx requires lots of trial-and-error search. You can test regular expressions online before including them into your program:
http://www.regexplanet.com/simple/

Characters used in RegEx patterns:
Some of the most commonly used characters in Regular Expression patterns are:
\d    	- decimal character [0..9]
\w    	- alphanumeric [a..z] or [0..9]
\A	- start of the text
\Z	- end of the text
[ABC] 	- one of characters A,B,C
.     	- any character
^A   	- not A
a+     	- one or more of pattern a
a*	- zero or more of pattern a
a|b   	- either pattern a or b matches
\s       - empty space 
Ignoring case
If the case of the text should be ignored during the pattern matching, add re.IGNORECASE to the parameters of any re function.
Managing files and directories
Change the current directory
With the os module, you can change the current directory:
import os
os.chdir(''..\\python'')
Listing files in a directory
os.listdir(''..\\python'')
Check whether a file exists
print os.access('my_file.txt')
Installable Packages
Creating plots
The Matplotlib library contains a wide range of possibilities for creating graphs. See the 'gallery' link on http://matplotlib.sourceforge.net for examples. It needs to be installed separately.
from pylab import *
Number crunching
Numpy is a library that allows operating on arrays and matrices. It needs to be installed separately. See: http://numpy.scipy.org
import numpya = numpy.array( [1,2,3,4,5,6] )print a+10, a*a
Image manipulation
The Python Imaging Library PIL is a powerful tool for working with images (changing formats, resizing, cutting, drawing). It needs to be installed separately. See http://www.pythonware.com/products/pil .

