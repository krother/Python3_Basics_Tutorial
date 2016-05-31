
# Reading simple text files

## Preparations

For the first exercise, you need a data file `bigbang.txt` containing the following data:

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
Depending on your editor, you may need to insert the complete path to the file. If the program does not work, a wrong file name or location are by far the most probable reasons.


## Exercise 2

Write a program that calculates the total number of names in the file `bigbang.txt` from the dataset of baby names. 

You will need to use a counter variable. The follwing two lines will be useful:

    names = 0

and 

    names = names + 1


## Exercise 3

Write a program that reads a file `bigbang_numbers.txt` that contains numbers only and calculates their sum. For the file, use the following data:

    12562
    2178
    342
    129
    384
    208
    164
    82
    41

