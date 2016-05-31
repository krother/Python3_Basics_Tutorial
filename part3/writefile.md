
# Writing text files

## Warming up

Match the descriptions with the Python commands.

![file exercise](../exercises/files.png)

## Warming up

Execute the following program. Explain what happens.

    names = ['Adam', 'Bob', 'Charlie']

    f = open('boy_names.txt', 'w')
    for name in names:
        f.write(name + '\n')
    f.close()

Remove the `+ '\n'` from the code and run the program again. What happens?


## Exercise 1

Which are correct commands to work with files?

- [ ] `for line in open(filename):`
- [ ] `f = open(filename, 'w')`
- [ ] `open(filename).writelines(out)`
- [ ] `f.close()`


## The Challenge: Write a table

Given is the following data:

    names = ["Emma", "Olivia", "Sophia", "Isabella", 
             "Ava", "Mia", "Emily"]
    numbers = [20799, 19674, 18490, 16950, 
               15586, 13442, 12562]

Write a program that writes all names into a single text file.

## Extra Challenges

* Write each name into a separate line.
* Write the numbers into the same file.
* Write each number into the same line as the corresponding name.
