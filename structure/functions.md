
# Writing your own Functions

**🎯 Implement functions in Python**

Writing all instructions into a single sequence creates programs that are hard to debug.
Here, you learn to break the code down into smaller units: **functions**.

### In this chapter you learn:

| Bereich | Thema |
|---------|-------|
| 💼 | Calculate the mean and standard deviation |
| ⚙ | define functions |
| ⚙ | use function parameters |
| ⚙ | use `return` to deliver results |
| 🔀 | recursion |

----

### Exercise 1: Sum up

Write a function that calculates a sum from a list of numers.
Insert into the gaps: `amount`, `data`, `def`, `return`, `calc_sum', `+=`

    :::text
    ____ calc_sum(data):
        total = 0
        for n in ____:
            total ____ n
        ____ total

    amount = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]
    s = ____(____)
    print(s)

----

### Exercise 2: Percentage

Write a function that calculates a percentage value (0-100) from a list of numbers and a population size.
Use the following structure:

    :::python
    def calc_percentage(data, population):

        # insert your code here
        ...

        return percentage


    testdata = [1, 2, 3, 4]
    perc = calc_percentage(testdata, 100.0)
    if perc == 10:
        print("Test successful!")
    else:
        print(f"you got {perc}% instead of 10")

----

### Exercise 3: Mean

Write a function that calculates the mean value from the following numbers:

    :::python3
    def mean(daten):
        ...

    data = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]

    ...

Find out what the function should deliver with `return`.

----

### Exercise 4: Standard Deviation

The following program calculates the standard deviation from a list of numbers.
You would like to generalize the code, so that it can be used with other data sets.
Wrap the code for the calculation – but not the data – in a function.

    :::python3
    import math

    data = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]

    avg = mean(data)

    stdsum = 0.0
    for n in data:
        stdsum += (n - avg) ** 2
    variance = stdsum / len(data)
    stdev = math.sqrt(variance)

    print(f"Standard Deviation: {stdev:8.2f}")

----

### Exercise 5: Optional Parameters

Explain the program:

    :::python3
    def addition(a=2, b=2, c=2):
        return a + b + c


    print(addition(3, 3, 3))
    print(addition(3, 3))
    print(addition(3))
    print(addition())
    print(addition(b=4))
    print(addition(b=4, c=5))

----

### Exercise 6: Rekursion

Explain the code:

    :::python3
    def factorial(n):
        """Calculates the factorial of the given number."""
        if n > 1:
            return n * factorial(n - 1)
        else:
            return 1


    x = int(input('Please enter a number: '))
    y = factorial(x)
    print (f"The result is:\n{x}! = {y}}")
