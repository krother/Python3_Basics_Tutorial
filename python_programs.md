
# Writing Python programs

In the second part, we will write our first programs in Python


## 8. Writing programs

Open a text editor window. Type: 

    print("Hannah")
    print(1234)

Now save the text to a file with the name `first_program.py`.

Then run the program. 

* In **Canopy**, you do this by pressing the 'play' button.
* In **IDLE**, you can execute a program by pressing F5.
* On **Unix**, you go open a terminal (*a regular one, not IPython*) and write:

    python3 first_program.py


## Definitions

### Python programs

A Python program is simply a text file that contains Python statements. 
The Python interpreter reads the file and executes the statements line by line.

* All program files should have the extension `.py`
* Only one command per line is allowed.

### Developing programs on Unix

When developing on Unix, the first line in each Python program should be:

    #!/usr/bin env python3

### print

The command `print()` Writes textual output to the screen. It accepts one or more arguments in parentheses - all things that will be printed. You can print both strings and integer numbers. You can also provide variables as arguments to `print()`.

We need print because typing a variable name in a Python program does not give you any visible output.



## Exercises

### Exercise 8.1

Try:

    name = "Emily"
    year = 2000
    print(name, year)

Write into a program:

    name = "Emily"
    name

What happens?

