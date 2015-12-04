
# Definitions

## Lists

A list is a Python data type representing a sequence of elements. You can have lists of strings:

    names = ['Hannah', 'Emily', 'Madiosn', 'Ashley', 'Sarah']

and also lists of numbers:

    numbers = [25952, 23073, 19967, 17994, 17687]


## Accessing elements of lists

Using square brackets, any element of a list and tuple can be accessed. The first character has the index 0.

    print(names[0])    
    print(numbers[3])

Negative indices start counting from the last character.

    print(names[-1])


## Creating lists from other lists:

Lists can be sliced by applying square brackets in the same way as strings.

    names = ['Hannah', 'Emily', 'Sarah', 'Maria']
    names[1:3]      
    names[0:2]      
    names[:3]       
    names[-2:]

You can use slicing to create a copy:

    girls = names[:]

## Adding elements to a list

Add a new element to the end of the list:

    names.append('Marilyn')

## Removing elements from a list

Remove an element at a given index:

    names.remove(3)

Remove the last element:

    names.pop()

## Replacing elements of a list

You can replace individual elements of a list by using an index in an assignment operation:

    names[4] = 'Jessica' 

## Sorting a list

    names.sort()

## Counting elements

    names = ['Hannah', 'Emily', 'Sarah', 'Emily', 'Maria']
    names.count('Emily')

