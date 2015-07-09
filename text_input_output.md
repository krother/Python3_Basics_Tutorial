# 9. Text input and output

## Examples

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

### Escape characters

Strings may contain also the symbols: `\t` (tabulator), `\n` (newline), `\r` (carriage return), and `\\` (backslash).


## Exercises

### Exercise 9.1

Which `input` statements are correct?

- [ ] `a = input()`
- [ ] `a = input("enter a number")`
- [ ] `a = input(enter your name)`
- [ ] `a = input(3)`

### Exercise 9.2

Which `print` statements are correct?

- [ ] `print("9" + "9")`
- [ ] `print "nine"`
- [ ] `print(str(9) + "nine")`
- [ ] `print(9 + 9)`
- [ ] `print(nine)`

