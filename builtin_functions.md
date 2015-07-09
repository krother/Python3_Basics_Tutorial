
# Built-in functions

## Examples

### Determining the length of sequences

The *len()* functions returns an integer with the length of an argument. It works with strings, lists, tuples, and dictionaries.

    data = [0,1,2,3]
    len(data)  

### Creating lists of integer numbers
The *range()* function allows to create lists of numbers on-the-fly. There are two optional parameters for the start value and the step size.

    data = range(4)       # [0,1,2,3]
    data = range(1,5)     # [1,2,3,4]
    data = range(2,9,2)   # [2,4,6,8]
    data = range(5,0,-1)  # [5,4,3,2,1]

### Summing up numbers
The *sum()* of a list of integer or float numbers or strings can be calculated by the *sum()* function.

    data = [1,2,3,4]
    sum(data)

### Enumerating elements of lists
The *enumerate()* function associates an integer number starting from zero to each element in a list. This is helpful in loops where an index variable is required.

    fruits = ['apple', 'banana', 'orange']
    for i, fruit in enumerate(fruits):
        print(i, fruit)

### Merging two lists

The *zip()* function associates the elements of two lists to a single list or tuple. Excess elements are ignored.

    fruits = ['apple','banana','orange']
    prices = [0.55, 0.75, 0.80, 1.23]
    for fruit,price in zip(fruits, prices):	
        print(fruit, price)

### Other functions

* sorted(data) returns a sorted list
* map(f, data) applies a function to all elements.
* filter(f, data) returns elements for which f is True.
* reduce(f, data) collapses the data into one value.
