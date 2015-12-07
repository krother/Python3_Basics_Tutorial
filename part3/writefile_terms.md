
# Definitions

## Opening a file for writing

Writing text to files is very similar to reading. The only difference is the `'w'` parameter.

    f = open('my_file.txt','w')
    f.write(text)

If your data is a list of strings, it can be written to a file as a one-liner. You only need to add line breaks:

    lines = ['first line\n', 'second line\n']
    open('my_file.txt','w').writelines(lines)

## Appending to a file

It is possible to add text to an existing file, too.

    f = open('my_file.txt','a')
    f.write(text)
