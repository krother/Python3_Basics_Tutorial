
# Making decisions

The last missing piece in our basic set of commands is the ability to make decisions in a program. This is done in Python using the `if` command.


## Warming up

Add your favourite movie to the following program and execute it:

    movie = input('Please enter your favourite movie: ')
    if movie == 'Star Trek':
        print('Live long and prosper')
    elif movie == 'Star Wars':
        print('These are not the droids you are looking for')
    elif movie == 'Dirty Dancing':
        print('I fetched the melons')
    else:
        print("Sorry, I don't know the movie %s." % (movie) )


## Exercises

### Exercise 1

Which of these `if` statements are syntactically correct?

- [ ] `if a and b:`
- [ ] `if len(s) == 23:`
- [ ] `if a but not b < 3:`
- [ ] `if a ** 2 >= 49:`
- [ ] `if a != 3`
- [ ] `if (a and b) or (c and d):`

### Exercise 2

Write a program that lets the user enter a number on the keyboard. Find the number in the list that is closest to the number entered  and write it to the screen.

    data = [1, 2, 5, 10, 20, 100, 200, 500, 1000]
    query = int(input())


## The Challenge: Filter a list

You have a list of the top 20 girls names from 2000:

    ['Emily', 'Hannah', 'Madison', 'Ashley', 'Sarah', 
    'Alexis', 'Samantha', 'Jessica', 'Elizabeth', 'Taylor', 
    'Lauren', 'Alyssa', 'Kayla', 'Abigail', 'Brianna', 
    'Olivia', 'Emma', 'Megan', 'Grace', 'Victoria']

Write a program that prints all names that start with an `A`.

### Extra challenge

* count the number of names starting with `A` and print that number as well.
