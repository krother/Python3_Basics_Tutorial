
# Conditional loops with while

Control flow means controlling, which instruction is handled next. In this tutorial, we cover three of Pythons control flow statements: `for`, `if` and `while`.

## Exercise 1

Match the expressions so that the `while` loops run the designated number of times.

![while exercise](exercises/while.png)


## Exercise 2

Which of these `while` commands are correct?

- [ ] `while a = 1:`
- [ ] `while b == 1`
- [ ] `while a + 7:`
- [ ] `while len(c) > 10:`
- [ ] `while a and (b-2 == c):`
- [ ] `while s.find('c') >= 0:`

## Exercise 3

Which statements are correct?

- [ ] `while` is also called a conditional loop
- [ ] The expression after `while` may contain function calls
- [ ] It is possible to write endless `while` loops
- [ ] The colon after `while` may be omitted
- [ ] The code block after `while` is executed at least once

## Exercise 4

The following `for` loop searches for `33` in the data. Change the code so that it uses a `while` loop instead.

    data = [5, 7, 33, 12, 4, 3, 18]

    found = False
    for n in data:
        if n == 33:
            found = True

    print("The value 33 has been found: {}".format(found))

## Exercise 5

The following `while` loop counts numbers higher than 10.
Change the code so that it uses a `for` loop instead.

    data = [4, 7, 11, 1, 3,  15]

    i, j = 0,0
    while i < len(data):
        if data[i] > 10:
            j += 1
        i += 1
    
    print("Values higher than 10: {}".format(j))

## Exercise 6

Will the following `while` loop finish?

    count = 0
    while count > 0:
        print count
        count += 1

### Exercise 6

Will the following `while` loop finish?

    text = "a"
    while "z" not in text:
        text += "a"

### Exercise 7

Will the following `while` loop finish?
than
    a = 7
    b = 135
    while a != b:
        a += (a - b) / 10.0
        b -= (a - b) / 10.0

### Exercise 8

Will the following `while` loop finish?

    n = 0
    while n * 5 != n ** 2:
        n += 2

### Exercise 9

Will the following `while` loop finish?

    data = [1,2,7,8]
    while data[-1] > 2:
        data.pop()

### Exercise 10

Will the following `while` loop finish?

    data = [2,3,15]
    while data[0] < 100:
        data = data[1:]
