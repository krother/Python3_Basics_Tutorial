
# String methods

### Exercise 1

Determine what the expressions do to the string in the center.

![string exercise](../images/strings.png)

### Exercise 2

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
