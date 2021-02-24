
# Conditional Loops

In this chapter, you will learn a new way to influence the order in which instructions are executed (called *control flow*): Conditional loops or `while` loops.

----

### Exercise 1

Match the expressions so that the `while` loops run the designated number of times.

![while exercise](exercises/while.png)

----

### Exercise 2

Which of these `while` commands are correct?

    :::python3
    while a = 1:

    while b == 1

    while a + 7:

    while len(c) > 10:

    while a and (b-2 == c):

    while s.find('c') >= 0:

----

### Exercise 3

Which statements are correct?

- `while` is also called a conditional loop
- The expression after `while` may contain function calls
- It is possible to `while` loops that run forever
- The colon after `while` may be omitted
- The code block after `while` is executed at least once

----

### Exercise 4

The following `for` loop searches for `33` in the data. 
Modify the code, so that it uses a `while` loop instead.

    :::python3
    data = [5, 7, 33, 12, 4, 3, 18]

    found = False
    for n in data:
        if n == 33:
            found = True

    print("The value 33 has been found: {}".format(found))

---

### Exercise 5

The following `while` loop counts numbers higher than 10.
Change the code so that it uses a `for` loop instead.

    :::python3
    data = [4, 7, 11, 1, 3,  15]

    i = 0
    high = 0
    while i < len(data):
        if data[i] > 10:
            high += 1
        i += 1
    
    print(f"There are {high} values higher than 10")

----

### Exercise 6

Which of the following `while` loops will finish?

#### Exercise 6.1

    :::python3
    count = 0
    while count > 0:
        print count
        count += 1

#### Exercise 6.2

    :::python3
    text = "a"
    while "z" not in text:
        text += "a"

#### Exercise 6.3

    :::python3
    a = 7
    b = 135
    while a != b:
        a += (a - b) / 10.0
        b -= (a - b) / 10.0

#### Exercise 6.4

    :::python3
    n = 0
    while n * 5 != n ** 2:
        n += 2

#### Exercise 6.5

    :::python3
    data = [1, 2, 7, 8]
    while data[-1] > 2:
        data.pop()

#### Exercise 6.6

    :::python3
    data = [2, 3, 15]
    while data[0] < 100:
        data = data[1:]
