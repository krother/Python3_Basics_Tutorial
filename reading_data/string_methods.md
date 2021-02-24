
# String methods

### Exercise 1

The following program identifies names used for both girls and boys and writes them to a file.

Complete the code to dissect lines to columns, so that the variables `name` and `gender` are defined.


    girls = []
    duplicates = []

    for line in open('names/yob2015.txt'):

        # insert your code here

        if gender == 'F':
           girls.append(name)
        elif gender == 'M':
           if name in girls:
               duplicates.append(name)

    output = open('duplicate_names.txt', 'w')
    for name in duplicates:
        text = "{:>15s}\n".format(name)
        output.write(text)
    output.close()

----

### Exercise 2: Format Strings

Try the following expressions in a Python shell:

    "{}".format("Hello")
    "{:10}".format("Hello")
    "{:>10}".format("Hello")
    "{1} {0}".format("first", "second")
    "{:5d}".format(42)
    "{:4.1f}".format(3.14159)
    "{:6.3f}".format(3.14159)


### Exercise 3

You have the following two lists:

    top_ten_names = ['Jacob', 'Michael', 'Matthew', 'Joshua', \
        'Christopher', 'Nicholas', 'Andrew', 'Joseph', \
        'Daniel', 'Tyler']

    top_ten_numbers = [34465, 32025, 28569, 27531, \
        24928, 23632, 22818, 22307, 21500]

Write a program that creates a table with two vertically aligned columns.

### Exercise 4

Write a `for` loop producing the following string:

    000111222333444555666777888999
