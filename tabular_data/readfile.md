
# Reading Text Files

In this chapter, you will learn to extract information from simple text files.

## The dataset of U.S. baby names

![Babynamen](../images/baby.png)

For the next exercises, you will need to download a data set of baby names.
The authorities of the United States have recorded the first names of all people born as U.S. citizens since 1880. The dataset is publicly available on [http://www.ssa.gov/oact/babynames/limits.html
](http://www.ssa.gov/oact/babynames/limits.html). For the protection of privacy only names used at least 5 times appear in the data.

Download the shorter archive of baby names (not grouped by states) from [http://www.ssa.gov/oact/babynames/limits.html](http://www.ssa.gov/oact/babynames/limits.html).

### Exercise 1

Create a text file `bigbang.txt` in a text editor, containing the following data:

    Emily,F,12562
    Amy,F,2178
    Penny,F,342
    Bernadette,F,129
    Leonard,M,384
    Howard,M,208
    Sheldon,M,164
    Stuart,M,82
    Raj,M,41



## Exercise 1:

Make the program work by inserting `close`, `line`, `bigbang.txt`, `print` into the gaps.

    f = open(___)
    for ____ in f:
        ____(line)
    f.____()

#### Hint:

Depending on your editor, you may need to insert the complete path to the file. If the program does not work, a wrong file name or location are the most probable reasons.


### Exercise 3

How many different *girls names* were there in 2015?

**Sort** the following code lines and **indent them correctly**:

    girls = 0

    if "B" in line:

    print(girls)

    if ",F," in line:

    for line in open('names/yob2015.txt'):

    girls += 1


### Exercise 4

Extend the program from the previous exercise such that boys and girls names are counted separately.


### Exercise 5

Write a program that reads lines from the file `yob2015.txt`. Identify all lines containing your name and print them to the screen.
