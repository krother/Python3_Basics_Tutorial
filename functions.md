
## Functions

### What is a function?
A function is an autonomous sub-program with local variables, input and output, and its own namespace. 
In Python, a function definition must be followed by a code block:

    def calc_price(fruit,n):	
    '''Returns the price of fruits.'''
        if fruit=='banana':
            return 0.75 * n

    print(calc_price('banana',10))

### Optional parameters

Function parameters may have default values. In that case, they become optional. Do not use mutable types as default arguments!

    def calc_price(fruit, n=1): 
        ..

    print(calc_prices('banana'))
    print(calc_prices('banana',100))

### List and keyword parameters

You can add a list &#42;args for an unspecified number of extra parameters, or a dictionary &#42;&#42;kwargs for keyword parameters.

    def func(&#42;args, &#42;&#42;kwargs):
        print(args, kwargs)

    func(1, 2, a=3, b=4)

### Return values

A function may return values to the program part that called it. 

    return 0.75

Multiple values are returned as a tuple. 

    return 'banana', 0.75

In any case, the return statement ends the execution of a function.

