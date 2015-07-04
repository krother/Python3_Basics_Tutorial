
# 5. Text

So far, we have only worked with numbers. Now we will work with text as well.

    first = 'Emily'
    last = "Smith"
    first
    last

    name = first + " " + last
    name

What do the following statements do:

    name[0]

    name[3]
    
    name[-1]


## Definitions

### String

Text values are called **strings**. In Python, strings are defined by single quotes, double quotes or three quotes of either. The following are equivalent:

    first = 'Emily'
    first = "Emily"
    first = '''Emily'''
    first = """Emily"""

### String arithmetics

The operator `+` also works for strings, only that it concatenates the strings. It does not matter whether you write the strings as variables or as explicit values. 

The following three statements are equivalent:

    name = first + last
    name = first + "Smith"
    name = "Emily" + "Smith"

### Indexing

Using square brackets, any character of a string can be accessed. This is called **indexing**. The first character has the index `[0]`, the second `[1]` and the fourth has the index `[3]`.

    name[0]
    name[3]

With negative numbers, you can access single characters from the end, the index `[-1]` being the last, `[-2]` the second last character and so on:

    name[-1] 
    name[-2] 

Note that none of these modify the contents of the string variable.


## Exercises

### Exercise 5.1: Special characters

Is it possible to include the following characters in a string?

    . 7 @ ? / & * \ Ä ß " '

### Exercise 5.2: 

What do the following statements do?

    first = `Hannah`

    first = first[0]

    name = first

    name = ""

### Exercises 5.3: A data record

| first name | Andrew   |
|------------|----------|
| last name  | O'Malley |
| gender     | M |
| year of birth | 2000  |

Write the information from each row of the table into a string variable, then combine them to a single string, e.g.:

    O'Malley, Andrew, M, 2000
