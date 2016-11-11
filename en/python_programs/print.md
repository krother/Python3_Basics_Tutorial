
# Writing to the screen

In this section, you will write your first Python program. It will be the most simple Python program possible. We simply will have the program write names of babies to the screen.


## Warming up

Open a text editor window (*not a Python console*). Type: 

    print("Hannah")
    print(23073)

Now save the text to a file with the name `first_program.py`.

Then run the program. 

* In **Canopy**, you do this by pressing the 'play' button.
* In **IDLE**, you can execute a program by pressing F5.
* On **Unix**, you go open a terminal (*a regular one, not IPython*) and write:

    python3 first_program.py


## Exercises

### Exercise 1

Explain the following program:

    name = "Emily"
    year = 2000
    print(name, year)

### Exercise 2
Write into a program:

    name = "Emily"
    name

What happens?


### Exercise 3

Which `print` statements are correct?

- [ ] `print("9" + "9")`
- [ ] `print "nine"`
- [ ] `print(str(9) + "nine")`
- [ ] `print(9 + 9)`
- [ ] `print(nine)`


## The Challenge: Write a table with names

Many names of fictious characters that have been used as baby names.
Write a program that produces an output similar to:

    Harry      Hermione      Severus
    Tyrion     Daenerys      Snow
    Luke       Leia          Darth

### Extra challenges:

* Use a single `print` statement to produce the output.
* Store the names in separate variables first, then combine them.
* Use string formatting.
