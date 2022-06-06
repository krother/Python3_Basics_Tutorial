
# Writing Files

### Exercise 1: 

Form pairs of Python commands and their meanings.

![file exercise](../images/files.png)


### Exercise 2: Write a file

Execute the following program. Explain what happens.

    names = ['Adam', 'Bob', 'Charlie']

    f = open('boys.txt', 'w')
    for name in names:
        f.write(name + '\n')
    f.close()


### Exercise 3: New lines

Remove the `+ '\n'` from the program and execute it again. What happens?

----

### Exercise 5: f-Strings

Try the following commands in a Python shell:

    :::python3
    name = "Ada"
    number = 42
    pi = 3.14159

    print(f"{name}")
    print(f"{name:>10}")
    print(f"{number:5d}")
    print(f"{number:05d}")
    print(f"{pi:4.1f}")
    print(f"{pi:6.3f}")
    print(f"name: {name}    number: {number}    pi: {pi:6.3f}")

----

### Exercise 6: Table to string

Create a single comma-separated string from the nested list in exercise 4 and print it.

You can concatenate a list of strings with:

    :::python3
    text = '\n'.join(rows)

----

### Exercise 7: Table to file

Write the formatted data from exercise 6 to a CSV file.
