# Repeating instructions

In our early programs, each Python instruction was executed only once. That makes programming a bit pointless, because our programs are limited by our typing speed.

In this section we will take a closer look at the `for` statement that repeats one or more instructions several times.


## Exercise 1

What does the following program do?

    for number in range(1, 43):
        print(number)

### Exercise 2

What advantages does the `for` loop have over the following one?

    print(0)
    print(1)
    print(2)
    print(3)
    print(4)
    ..


### Exercise 3

Write a for loop that creates the following output

    1
    4
    9
    16
    25
    36
    49


### Exercise 4


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


### Exercise 5

What does the following program do?

    text = ""
    characters = "Hannah"
    for char in characters:
        text = char + text
    print(text)


## Exercise 6

Write a program that calculates the number of characters in `Stefani Joanne Angelina Germanotta`. **Spaces count as well!**
