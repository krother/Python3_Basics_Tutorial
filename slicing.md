
# Slicing strings and lists

## Creating substrings

Substrings can be formed by applying square brackets with two numbers inside separated by a colon (slices). The second number is not included in the substring itself.

    s = 'Manipulating Strings'
    s[1:6]
    s[9:13]
    s[0:2]
    s[:3] 
    s[-4:] 


## Creating lists from other lists:

Lists can be sliced by applying square brackets in the same way as strings.

    data = [0,1,2,3,4,5]
    data[1:3]      # [1,2]
    data[0:2]      # [0,1]
    data[:3]       # [0,1,2]
    data[-2:]      # [4,5]
    m = data[:]    # creates a copy!


## Exercises

### Exercise 1

Use the expressions to modify the list as indicated. Use each expression once.

![list funcs exercise1](exercises/list_funcs1.png)

### Exercise 2

What does the list b contain?

    a = [8, 7, 6, 5, 4]
    b = a[2:4]

- [ ] `[7, 6, 5]`
- [ ] `[7, 6]`
- [ ] `[6, 5]`
- [ ] `[6, 5, 4]`

