
# Reading and writing files

IO: eine Tabelle mit Babynamen laden
  IO: das Textformat CSV kennen lernen
  OS: read all files
  
## Exercise

Match the descriptions with the Python commands.

![file exercise](exercises/files.png)

## Definitions

### Opening a file for reading

Text files can be accessed using the `open()` function. From an open file the contents can be read as a string.

    f = open('my_file.txt')
    text = f.read()

An open file behaves like a list of strings. Thus, it is possible to read it line by line without using `s.split('\n')`:

    for line in open('my_file.txt'):
	    name = line[:10].strip()
	    print(name.strip())

### Opening a file for writing

Writing text to files is very similar. The only difference is the `'w'` parameter.

    f = open('my_file.txt','w')
    f.write(text)

If your data is a list of strings, it can be written to a file as a one-liner. You only need to add line breaks:

    lines = ['first line\n', 'second line\n']
    open('my_file.txt','w').writelines(lines)

### Appending to a file

It is possible to add text to an existing file, too.

    f = open('my_file.txt','a')
    f.write(text)

### Closing files

Closing files in Python is not mandatory but good practice.

    f.close()

## Writing directory names in Python

When opening files, you can use full or relative directory names. However, you must replace the backslash `\` by a double backslash `\\` (because `\` is also used for escape sequences like `\n` and `\t`).

    f = open('..\\my_file.txt')
    f = open('C:\\python\\my_file.txt')

## Exercises

### Exercise 1

Which are correct commands to work with files?

- [ ] `for line in open(filename):`
- [ ] `f = open(filename, 'w')`
- [ ] `open(filename).writelines(out)`
- [ ] `f.close()`

