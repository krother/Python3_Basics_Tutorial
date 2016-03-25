# Repeating instructions

So far, each Python instruction was executed only once. That makes programming a bit useless, because our programs are limited by our typing speed.

In this section you will learn the `for` statements that repeats one or more instructions several times.


## Warming up

What does the following program do?

    text = ""
    characters = "Hannah"
    for char in characters:
        text = char + text
    print(text)


## Exercises

### Exercise 1

Which of these `for` commands are correct?

- [ ] `for char in "ABCD":`
- [ ] `for i in range(10):`
- [ ] `for num in (4, 6, 8):`
- [ ] `for k in 3+7:`
- [ ] `for (i=0; i<10; i++):`
- [ ] `for var in seq:`

### Exercise 2

Write a for loop that creates the following output

    000
    111
    222
    333
    444
    555
    666
    777
    888
    999

### Exercise 3

Write a for loop that creates the following string variable:

    000111222333444555666777888999

### Exercise 4

Write a for loop that creates the following output

    1
    3
    6
    10
    15
    21
    28

### Exercise 5

Write a for loop that creates the following string

    "1 4 9 16 25 36 49 64 81 "

### Exercise 6

Add a single line at the end of the program, so that it creates the following string:

    "1 4 9 16 25 36 49 64 81"


## The Challenge: count characters

Write a program that calculates the number of characters in `Emily Smith`.

### Extra challenge

* Duplicate each character, so that `Emily` becomes `EEmmiillyy`.
