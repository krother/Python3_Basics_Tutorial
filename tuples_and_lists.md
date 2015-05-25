
# Tuples and Lists

## Tuples

A tuple is a sequence of elements that cannot be modified. They are useful to group elements of different type. 

    t = ('bananas','200g',0.55)

In contrast to lists, tuples can also be used as keys in dictionaries.

## Lists

A list is a sequence of elements that can be modified. In many cases, all elements of a list will have the same type.

    data = ['apples', 'bananas', 'oranges']

## Accessing elements of lists and tuples

Using square brackets, any element of a list and tuple can be accessed. The first character has the index 0.

    data = [1,2,3,4]
    print data[0]    # first
    print data[3]    # last
    print data[-1]   # last
    data[0] = 'kiwi' # assigning an element

## Creating lists from other lists:

Lists can be sliced by applying square brackets in the same way as strings.

    data = [0,1,2,3,4,5]
    data[1:3]      # [1,2]
    data[0:2]      # [0,1]
    data[:3]       # [0,1,2]
    data[-2:]      # [4,5]
    m = data[:]    # creates a copy!

## List methods

Lists provide many useful methods:

    data[0] = 'kiwi' # assigns an element

#### Adding elements to a list:

    data.append(5)   # adds at the end

#### Removing elements from a list:

    data.remove(3)
    data.pop()       # removes last element

#### Sorting a list:

    data.sort()

#### Counting elements:

    data.count(3)


## Built-in functions working on iterable types

#### Determining the length of sequences
The *len()* functions returns an integer with the length of an argument. It works with strings, lists, tuples, and dictionaries.

    data = [0,1,2,3]
    len(data)  

#### Creating lists of integer numbers
The *range()* function allows to create lists of numbers on-the-fly. There are two optional parameters for the start value and the step size.

    data = range(4)       # [0,1,2,3]
    data = range(1,5)     # [1,2,3,4]
    data = range(2,9,2)   # [2,4,6,8]
    data = range(5,0,-1)  # [5,4,3,2,1]

#### Summing up numbers
The *sum()* of a list of integer or float numbers or strings can be calculated by the *sum()* function.

    data = [1,2,3,4]
    sum(data)

#### Enumerating elements of lists
The *enumerate()* function associates an integer number starting from zero to each element in a list. This is helpful in loops where an index variable is required.

    fruits = ['apple', 'banana', 'orange']
    for i, fruit in enumerate(fruits):
        print(i, fruit)

#### Merging two lists

The *zip()* function associates the elements of two lists to a single list or tuple. Excess elements are ignored.

    fruits = ['apple','banana','orange']
    prices = [0.55, 0.75, 0.80, 1.23]
    for fruit,price in zip(fruits, prices):	
        print(fruit, price)

#### Other functions

* sorted(data) returns a sorted list
* map(f, data) applies a function to all elements.
* filter(f, data) returns elements for which f is True.
* reduce(f, data) collapses the data into one value.

