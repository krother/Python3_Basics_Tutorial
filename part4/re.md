
# re

## What is re?

`re` is a Python module for *Regular Expressions*. Regular expressions help you to search and replace text using sophisticated patterns.

## Searching

    import re

    text = 'all ways lead to Rome'

    # find one occurence
    print(re.search('R...\s', text))

    # find every occurence
    print(re.findall('\s(.o)', text))

## Replacing

    re.sub('R[meo]+', 'London', text)

### How to find the right pattern for your problem:
Finding the right RegEx requires lots of trial-and-error search. You can test regular expressions online before including them into your program:
[www.regexplanet.com/simple/](http://www.regexplanet.com/simple/)

### Characters used in RegEx patterns:
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

### Ignoring case
If the case of the text should be ignored during the pattern matching, add `re.IGNORECASE` to the parameters of any `re` function.

## Exercises

### Exercise 1

Write six patterns that extract all names from the following string:
  
    "In the class were three girls: Thelma, Emma and 
    Sophia. Also three boys: Emmett and his best friends 
    Sophocles and Theophilius" 

### Exercise 2

Reduce the number of patterns you need to three.

### Exercise 3

Find all six names using a single pattern.

## Where to learn more about Regular Expressions?

    see [www.regexone.com](http://www.regexone.com)
