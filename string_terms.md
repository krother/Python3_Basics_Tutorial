
# Definitions

## String

Text values are called **strings**. In Python, strings are defined by single quotes, double quotes or three quotes of either. The following are equivalent:

    first = 'Emily'
    first = "Emily"
    first = '''Emily'''
    first = """Emily"""

## String arithmetics

The operator `+` also works for strings, only that it concatenates the strings. It does not matter whether you write the strings as variables or as explicit values. 

The following three statements are equivalent:

    name = first + last
    name = first + "Smith"
    name = "Emily" + "Smith"

## Indexing

Using square brackets, any character of a string can be accessed. This is called **indexing**. The first character has the index `[0]`, the second `[1]` and the fourth has the index `[3]`.

    name[0]
    name[3]

With negative numbers, you can access single characters from the end, the index `[-1]` being the last, `[-2]` the second last character and so on:

    name[-1] 
    name[-2] 

Note that none of these modify the contents of the string variable.
