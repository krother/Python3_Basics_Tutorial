
# Tutorial: Introduction to Python for programmers

This is a 60-90' introductory tutorial to the Python language for people with programming experience.

## Objective

In this tutorial, you will:

1. Run a Python program.
2. Use basic input and output functions.
3. Use basic data types.
4. Use `for` loops and branching with `if`.
5. Modularize code.

## Preparations

* Download and unzip the [Code Examples [ZIP]](files/python_shopping_list.zip).
* Download the e-book [Python 3 Basics](https://krother.gitbooks.io/python-3-basics-tutorial/content/) as a quick reference of Python Commands.
* Install [Python3.4](http://www.python.org) or higher.
* Make sure you can invoke Python from the command line by typing `python`. You should see a prompt `>>>`. Leave the Python console by `Ctrl-D` or `Ctrl-Z`.
* Open a text editor with syntax highlighting (Sublime, IDLE, emacs, Notepad++)

## Problem description
You want to check how much money you have spent recently on shopping. You wrote everything you have bought into a tab-separated text file (`bill.txt`). 

| item | price |
|------|-------|
| tomatoes | 4 |
| potatoes | 5 |
| pizza | 17 |
| tomatoes | 3 |
| coffee | 5 |
| tomatoes | 7 |
| bread | 4 |
| coffee | 5 |
| tomatoes | 2 |
| coffee | 5 |

## Exercise 1: Warming up

Which items was the most money spent on? How much? 

Write down the numbers before moving on.


## Exercise 2: Running a Python program

Open the program `shopping.py` in the editor. Execute the program from the console by typing 

    python shopping.py

### Task 1.1
Make sure the program and you get the same result.

## Exercise 2: Using print

In *Python 3 Basics* in **3.1 - Text input and output**, you will find examples for the `print` command.

### Task 2.1
Write a *“hello world”* program in Python.

### Task 2.2
Add three print statements to `shopping.py` to display the values of variables. Run the program and make sure it works.

## Exercise 3: Data types in Python

### Task 3.1
Write a program that reads two numbers from the keyboard, converts them to floating-point numbers, and prints their sum. You will need the functions `float()` and `input()` explained in the reference.

### Task 3.2
Which of the following data types is **not** used in `shopping.py`? 

* list
* string
* float
* dictionary
* integer

## Exercise 4: Using lists
For this exercise, you will need **3.3 - Lists** and **3.4 - Builtin functions** from the reference.

### Task 4.1
Write a program that uses the `range()` function to create a list with numbers from 1 to 10. Print the first five numbers from the list.

### Task 4.2
Add a `for` loop that prints each number in the list.

### Task 4.3
Add a `for` loop at the end of `shopping.py` to print the result in separate lines.

## Exercise 5: Branching

### Task 5.1
Add an `if` statement to the `for` loop from **Task 4.2** to print only even numbers (`2, 4, 6, ..`).

### Task 5.2
Change `shopping.py` in such a way that only every second line from the file is used.

## Exercise 6: Using dictionaries

### Task 6.1
Sort the lines in `dictionary_example.py` so that the program runs.

### Task 6.2

| item | price |
| tomatoes | 6 | 
| bicycle | 300 | 
| bus ticket | 2 |

Add a few lines of code to `shopping.py` so that after reading the file, the three extra items from the table are added to items. **Do not edit the text file `bill.txt`**:

## Exercise 7: Using functions

### Task 7.1
Take a look at the program `function_example.py`. Modify the program `shopping.py` program in such a way that it does the same thing as before, but uses two functions:

* **parse_items** – gets a filename and returns a list of `(item, value)` pairs.
* **calc_max3** – gets a list of `(item, value)` pairs and returns the three most expensive groups of items.

## Exercise 8: Using classes

### Task 8.1
Take a look at the program `class_example.py`. Modify the `shopping.py` program in such a way that it does the same thing as before, but uses one class `MaxItemsCalculator` with methods that work similar to the functions in Exercise 7. Use attributes of the instance `self` to store the results.

## Exercise 9: Importing modules

### Task 9.1
Execute the program `import_example.py` that uses the `MaxItemsCalculator` class. Make it work.
