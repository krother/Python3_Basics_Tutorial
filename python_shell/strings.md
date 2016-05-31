
# Storing text

## Warming up

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


## Exercises

### Exercise 1: 

Is it possible to include the following special characters in a string?

    . 7 @ ? / & * \ Ä ß " ' á

### Exercise 2: 

What do the following statements do?

    first = `Hannah`

    first = first[0]

    name = first

    name = ""

### Exercise 3:

Explain the code

    text = ""
    characters = "ABC"
    text = characters[0] + text
    text = characters[1] + text
    text = characters[2] + text
    text

## The Challenge

| first name | Andrew   |
|------------|----------|
| last name  | O'Malley |
| gender     | M |
| year of birth | 2000  |

Write the information from each row of the table into a separate string variable, then combine them to a single string, e.g.:

    O'Malley, Andrew, M, 2000

