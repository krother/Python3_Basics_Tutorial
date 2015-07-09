
#
## 7. Writing programs

Open a text editor window. Type: 

    print("Hannah")
    print(1234)

Now run the program by pressing the 'play' button.

#### Definition: print

#### Definition: Python-Interpreter

#### Exercise

Also try:

    name = "Emily"
    year = 2000
    print(name, year)

Write into a program:

    name = "Emily"
    name

What happens?

 Python Programs

* All program files should have the extension `.py`
* Indentation is a central element of Python syntax, marking code blocks. Code blocks should be indented by four spaces/one tab. Indentation must not be used for decorative purposes.
* Only one command per line is allowed.

### Developing programs on Unix

When developing on Unix, the first line in each Python program should be:

    #!/usr/bin env python


## Comments

In Python, single lines can be commented by the hash symbol (`#`):

    # this is a comment.
    print(a + b)  # adding the variables

Also, multi-line comments can be enclosed by triple quotes:

    '''
    This is a longer description
    that stretches over multiple lines.
    '''

#### Hint
The triple quoted comments can be used to generate documentation automatically. 

## Quiz Questions

#### 1. Which lines are commented?

- [ ] `"""This is a comment"""`
- [ ] `# This is a comment`
- [ ] `// This is a comment`
- [ ] `<!-- This is a comment !-->`
- [ ] `'''This is a comment'''`

* Writing code blocks with 2+ lines in the CLI gets painful quickly.
* From IDLE, you can execute a program in the command line by pressing F5.
