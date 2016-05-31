# String methods 

## Exercise

Find out what each of the expressions does to the string in the center.

![string exercise](../exercises/strings.png)

## Definitions

### String methods

Every string in Python brings a list of functions to work with it. As the functions are contained within the string they are also called **methods**. They are used by adding the `.` to the string variable followed by the method name.

Below you find a few of the available methods:

### Changing case:

    s = 'Manipulating Strings '
    s.upper()
    s.lower()

### Removing whitespace at both ends:

    s.strip()

### Cutting a string into columns:

    s.split(' ')

### Searching for substrings: 

    s.find('ing')

The method returns the start index of the match. The result -1 means that no match has been found.

### Replacing substrings:

    s.replace('Strings','text')

### Removing whitespace at both ends: 

    s.startswith('Man')
    s.endswith('ings') 

