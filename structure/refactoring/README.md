
# Cleaning Up

Cleaning up code is an everyday activity of any prorammer. Clean programs are shorter, easier to understand and easier to change. The process of cleaning up is also called **refactoring**.
In this chapter, you will learn basic techniques to refactor a program.

The code below is a full implementation of a simple *"Connect Four"* game. The program is working. If you manage to write a program of that size for the first time, it is a huge success! That success is not made smaller if the code is dirty and requires clean-up. The program below is not very well-written. It contains lots of problematic regions.

### Exercise 1

Read the code. What problems might the code contain.

## Refactor

Refactoring means **improving the structure of a program without changing its functionality.**

Here, we will apply the following refactorings:

* extract a variable
* extract a loop
* extract function
* split a function
* merge redundant blocks
* introduce a state variable
* introduce a __main__ block
