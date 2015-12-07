
# Definitions

## The strip/split pattern

The two most frequently written lines you need in Python are probably:

for line in open(filename):
    columns = line.strip('\n').split(sep)
    ...

This pattern goes through a file line by line (the `for` line). It then chops off a linebreak character from each line (`strip`) and finally breaks the line into a list of items.

## str.strip()

With the string function `strip()`, you chop off whitespace characters (spaces, newline characters and tabs) from both ends of a string.

The line

    text = "  this is text   "
    s = text.split()

produces:

    print(s)
    
    "this is text"

## str.split()

With the string function `split(x)`, you can divide a string into a list of strings. `x` is the character at which you want to separate the columns (by default whitespace).

    s = "this is text"
    t = s.split(" ")
    print(t)

    ["this", "is", "text"]
    
Both functions perfectly complement each other.
