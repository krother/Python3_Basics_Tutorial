

## 9. Lists

## Using a list

Find out what each of the expressions does to the list in the center.

![list exercise](exercises/lists.png)


## Definitions

### Lists

A list is a sequence of elements that can be modified. In many cases, all elements of a list will have the same type.

    data = ['apples', 'bananas', 'oranges']


### Accessing elements of lists

Using square brackets, any element of a list and tuple can be accessed. The first character has the index 0.

    data = [1,2,3,4]
    print(data[0])    
    print(data[3])

Negative indices start counting from the last character.

    print(data[-1])

### Assigning to elements of a list

You can replace individual elements of a list by using an index in an assignment operation:

    data[0] = 'kiwi' 

