
# Lists

In this chapter we will combine multiple values to a new data type: a **list**.

To process larger amounts of data, we cannot invent a new variable name for every entry (and write the code for it).
Somehow it has to be possible to store multiple data records in one variable.
This is where **lists** come in.

Lists are a simple sequence of elements.
However, Python is counting differently than humans:

![Indexing](indexing.png)

----

### Exercise 1

Try a few commands for creating lists:

    numbers = [1, 2, 4, 8, 16, 32]
    numbers = numbers + [64, 128, 256]
    print(numbers)

    for num in numbers:
        print(f)

Write code to print all the movie names:

    movies = ["Star Wars", "Star Trek", "Ratatouille"]
    movies += ["Arrival"]

    ...

----

### Exercise 2: Indexing

What do the following commands result in?

    numbers[4]

    movies[0]

    movies[-1]

    numbers[-3]

----

### Exercise 3: Slicing

What do the following commands result in?

    movies[2:]

    movies[:2]

    numbers[2:-2]

    numbers[::2]

----

### Exercise 4: List syntax

Which instructions are correct?

    ["Tilda", "Swinton"]`

    ["Darth Vader" "Yoda"]`

    [1, 2 + 3, 4]`

    [1, 2] + [3, 4]`

    [1, 2] + 3, 4]`

    [1, 2.0, "three"]`

----

### Exercise 5: List methods

Find out what each of the expressions does to the list in the center.

![list exercise](lists.png)


----

### Exercise 6: Puzzle

Use the expressions to modify the list as indicated. Use each expression once.

![list funcs exercise2](list_funcs2.png)

----

### Exercise 7: Another puzzle

Use the expressions to modify the list as indicated. Use each expression once.

![list funcs exercise1](list_funcs1.png)

---

### Exercise 8: Movie initials

Create a list that contains names of movies.
Write a `for` loop that iterates through the movie names.
Build a new list that contains only the first characters of each title.

For instance with the input:

    Star Wars, Star Trek, Ratatouille

your program should output

    S
    S
    R
