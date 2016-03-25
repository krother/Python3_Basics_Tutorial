
# Extracting information from a file

Rarely you can use the information from a file directly. Most of the time you will need to *parse* it, that is extracting relevant information.

Parsing means for instance:

* dividing tables into columns
* converting numbers to integers or floats.
* discarding unnecessary lines.


## Warming up

Create a text file in a text editor. Write the following line there:

    Alice Smith;23;Macroeconomics

Save the file with the name `alice.txt`.

Then run the following program:

    f = open('alice.txt')
    print(f)
    text = f.read()
    print(text)
    columns = text.strip().split(';')
    print(columns)
    name = columns[0]
    age = int(columns[1])
    studies = columns[2]
    print(name)
    print(age)
    print(studies)

What happens?

## Exercises

### Exercise 1

What does the following line produce?
  
    "Take That".split('a')

### Exercise 2

Create a text file with the contents:

    Alice Smith;23;Macroeconomics
    Bob Smith;22;Chemistry
    Charlie Parker;77;Jazz

Write a program that reads all names and puts them into a list. Print the list.

### Exercise 3

Collect the ages into a separate list.

### Exercise 4

Collect the occupations into a separate list.

### Exercise 5

Leave the `strip()` command away from the above program. What happens? 


## The Challenge: Find Your name

Write a program that finds out how often your name occurs in the list of 2014 baby names and print that number.

### Extra Challenge:

* Calculate the total number of babies registered in 2014.

