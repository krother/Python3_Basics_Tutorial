
# Definitions

## Python programs

A Python program is simply a text file that contains Python statements. 
The Python interpreter reads the file and executes the statements line by line.

* All program files should have the extension `.py`
* Only one command per line is allowed.

### Developing programs on Unix

When developing on Unix, the first line in each Python program should be:

    #!/usr/bin env python3

## print

The command `print()` Writes textual output to the screen. It accepts one or more arguments in parentheses - all things that will be printed. You can print both strings and integer numbers. You can also provide variables as arguments to `print()`.

We need print because typing a variable name in a Python program does not give you any visible output.

The Python print statement is very versatile and accepts many combinations of strings, numbers, function calls, and arithmetic operations separated by commas.

### Examples: 

    print('Hello World')
    print(3 + 4)
    print(3.4)
    print("""Text that 
    stretches over 
    multiple lines.
    """)
    print('number', 77)
    print()
    print(int(a) * 7)

### String formatting

Variables and strings can be combined, using formatting characters. This works also within a print statement. In both cases, the number of values and formatting characters must be equal.

    s = 'Result: %i' % (77)
    print('Hello %s!' % ('Roger')
    a = 5.099999
    b = 2.333333
    print('(%6.3f/%6.3f)' % (a, b)

The formatting characters include:

* `%i` – an integer.
* `%4i` – an integer formatted to length 4.
* `%6.2f` – a float number with 6 digits (2 after the dot).
* `%10s` – a right-oriented string with length 10.

### Escape characters

Strings may contain also the symbols: `\t` (tabulator), `\n` (newline), `\r` (carriage return), and `\\` (backslash).

