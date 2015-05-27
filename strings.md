
# Strings

Strings in Python can be defined by single quotes, double quotes or triple quotes. The following are equivalent:

    s = 'text'
    s = "text"
    s = '''text'''
    s = """text"""
    

### Exercise

Find out what each of the expressions does to the string in the center.

![string exercise](exercises/strings.png)

## Accessing individual characters

Using square brackets, any character of a string can be accessed. The first character has the index `0`.

    s = 'Manipulating Strings'
    s[0]  # first character
    s[3]
    s[-1] # last character
    s[-2] # second last

## Creating substrings

Substrings can be formed by applying square brackets with two numbers inside separated by a colon (slices). The second number is not included in the substring itself.

    s = 'Manipulating Strings'
    s[1:6]
    s[9:13]
    s[0:2]
    s[:3] 
    s[-4:] 

## Length of strings
Is returned as an integer by the `len()` function.

    print(len('Manipulating Strings'))

## String functions

The following functions work on every string variable.

    s = 'Manipulating Strings '

#### Changing case:

    s.upper()
    s.lower()

#### Removing whitespace at both ends:

    s.strip()

#### Cutting a string into columns:

    s.split(' ')

#### Searching for substrings: 

    s.find('ing')

#### Replacing substrings:

    s.replace('Strings','text')

#### Removing whitespace at both ends: 

    s.startswith('Man')
    s.endswith('ings') 


## Text input and output

### Reading from the text console
User input can be read from the keyboard with or without a message text. The value returned is always a string:

    a = input()
    a = input('Please enter a number')

### Writing to the text console: 
The Python print statement is very versatile and accepts almost any combination of strings, numbers, function calls, and  arithmetic operations separated by commas.

    print('Hello World')
    print(3 + 4)
    print(3.4)
    print("""Text that stretches over 
    multiple lines.""")
    print('number', 77)
    print()
    print(int(a) * 7)

### String formatting

Variables and strings can be combined, using formatting characters. This works also within a print statement. In both cases, the number of values and formatting characters must be equal.

    s = 'Result: %i' % (number)
    print('Hello %s!' % ('Roger')
    print('(%6.3f/%6.3f)' % (a, b)

The formatting characters include:

* `%i` – an integer.
* `%4i` – an integer formatted to length 4.
* `%6.2f` – a float number with 6 digits (2 after the dot).
* `%10s` – a right-oriented string with length 10.

#### Escape characters
Strings may contain also the symbols: `\t` (tabulator), `\n` (newline), `\r` (carriage return), and `\\` (backslash).


## Quiz Questions

#### 1. Which `input` statements are correct?

- [ ] `a = input()`
- [ ] `a = input("enter a number")`
- [ ] `a = input(enter your name)`
- [ ] `a = input(3)`

#### 2. Which `print` statements are correct?

- [ ] `print("9" + "9")`
- [ ] `print "nine"`
- [ ] `print(str(9) + "nine")`
- [ ] `print(9 + 9)`
- [ ] `print(nine)`

