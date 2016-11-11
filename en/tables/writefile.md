
# Writing text files

## Exercise 1

Match the descriptions with the Python commands.

![file exercise](../exercises/files.png)

## Exercise 2

Execute the following program. Explain what happens.

    names = ['Adam', 'Bob', 'Charlie']

    f = open('boy_names.txt', 'w')
    for name in names:
        f.write(name + '\n')
    f.close()

Remove the `+ '\n'` from the code and run the program again. What happens?

## Exercise 3

The following program writes names used for both boys and girls into a file.

Complete the part dissecting the line into the variables `name` and `gender`.


    girls = []
    duplicates = []

    for line in open('names/yob2014.txt'):
        
        # add your code here
        
        if gender == 'F':
           girls.append(name)
        elif gender == 'M':
           if name in girls:
               # found a duplicate name!
               duplicates.append(name)


    # write results to a file
    output = open('doppelnamen.txt', 'w')
    for name in duplicates:
        text = "{:>15s}\n".format(name)
        output.write(text)
    output.close()


## Exercise 4

Which are correct commands to work with files?

- `for line in open(filename):`
- `f = open(filename, 'w')`
- `open(filename).writelines(out)`
- `f.close()`


## Exercise 5

Given is the following data:

    names = ["Emma", "Olivia", "Sophia", "Isabella", 
             "Ava", "Mia", "Emily"]
    numbers = [20799, 19674, 18490, 16950, 
               15586, 13442, 12562]

Write a program that writes all data into a single text file.

## Extra Challenges

* Write each name into a separate line.
* Write the numbers into the same file.
* Write each number into the same line as the corresponding name.
