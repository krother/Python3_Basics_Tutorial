
# Making decisions

The last missing piece in our basic set of commands is the ability to make decisions in a program. This is done in Python using the `if` command.


## Exercise 1

Execute the following program. What does it calculate?

    boys = 0
    girls = 0
    for line in open('yob2014.txt'):
        if ",M," in line:
            boys = boys + 1
        elif ",W," in line:
            girls = girls + 1
        else:
            print("unrecognized line:", line)
    print(boys, girls)


## Exercise 2

Which of these `if` statements are syntactically correct?

* `if a and b:`
* `if len(s) == 23:`
* `if a but not b < 3:`
* `if a ** 2 >= 49:`
* `if a != 3`
* `if (a and b) or (c and d):`


## Exercise 3

Write a program that lets the user enter a name on the keyboard. Find the line(s) containing that name in the file `yob2014.txt` and write them to the screen.


## Exercise 4

You have a list of the top 20 girls names from 2000:

    ['Emily', 'Hannah', 'Madison', 'Ashley', 'Sarah', 
    'Alexis', 'Samantha', 'Jessica', 'Elizabeth', 'Taylor', 
    'Lauren', 'Alyssa', 'Kayla', 'Abigail', 'Brianna', 
    'Olivia', 'Emma', 'Megan', 'Grace', 'Victoria']

Write a program that prints all names that start with an `A`.


## Exercise 5

How many baby names are there in 1900 beginning with `M`?

How many in 2014?


## Exercise 6

How many different *girls* names starting with an `M` were there in 2014?

