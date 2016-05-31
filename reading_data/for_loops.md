# Repeating instructions

In our early programs, each Python instruction was executed only once. That makes programming a bit pointless, because our programs are limited by our typing speed.

In this section we will take a closer look at the `for` statement that repeats one or more instructions several times.


## Exercise 1

What does the following program do?

    for number in range(42):
        print(number)

What advantages does this program have over this one:

    print(0)
    print(1)
    print(2)
    print(3)
    print(4)
    ..


### Exercise 2

Write a for loop that creates the following output

    1
    4
    9
    16
    25
    36
    49


## Exercise 3


Explain the difference between the following two programs:

    total = 0
    for number in range(10):
        total = total + number
        print(total)

and

    total = 0
    for number in range(10):
        total = total + number
    print(total)


## Exercise 4

Write a for loop that creates the following string

    1 4 9 16 25 36 49 64 81


## Exercise 5

Write a for loop that creates the following string:

    000111222333444555666777888999


## Exercise 6

Which of these `for` commands are correct?

* `for char in "ABCD":`
* `for i in range(10):`
* `for number in [4, 6, 8]:`
* `for k in 3+7:`
* `for (i=0; i<10; i++):`
* `for var in open('bigbang.txt'):`


## Exercise 7

Read the file `bigbang_numbers.txt` and calculate the average and standard deviation. Use the code sniplet:

    import math
    root = math.sqrt(value)


## Exercise 8

What does the following program do?

    text = ""
    characters = "Hannah"
    for char in characters:
        text = char + text
    print(text)


## Exercise 9

Write a program that calculates the number of characters in `Emily Smith`.


## Exercise 10

Write a program that duplicates each character of a string, so that `Emily` becomes `EEmmiillyy`.

