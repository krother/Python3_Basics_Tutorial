# Using format strings

## Exercise 1

Try the following expressions on the Python shell:

    "{}".format("Hello")
    "{:10}".format("Hello")
    "{:>10}".format("Hello")
    "{1} {0}".format("First", "Second")
    "{:5d}".format(42)
    "{:4.1f}".format(3.14159)
    "{:6.3f}".format(3.14159)
        

## Exercise 2

The following program merges a list of names with a list of numbers and prints them to the screen.

The program **contains 3 defects**. Find and fix them.


    top_names = ['Jacob', 'Michael', 'Matthew', 'Joshua', 'Christopher', 
                 'Nicholas', 'Andrew' 'Joseph', 'Daniel', 'Tyler']

    top_numbers [34465, 32025, 28569, 27531, 24928,
                   24928, 23632, 22818, 22307, 21500]

    if len(top_names) == len(top_numbers):
       print("Warning: lists have different lengths!")
       print(len(top_names), len(top_numbers))

    for i in range(len(top_names)):
        name = top_names[i]
        number = top_numbers[i]
        print("{:10s} {:6d}".format(name, number))

