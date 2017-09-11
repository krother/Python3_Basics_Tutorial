
# a program that calculates factorials
# the factorial n! is 1*2*3*4 ... *n

def factorial(number):
    """Returns the factorial of the given number."""
    result = 1
    for i in range(1, number+1):
        result = result*i
    return result

x = int(input('Please enter an integer number: '))
y = factorial(x)
print ("Factorial: {}! = {}}".format(x, y))

