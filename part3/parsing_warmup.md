
# Warming up

Create a text file in a text editor. Write the following line there:

    Alice Smith;23;Macroeconomics

Save the file with the name `alice.txt`.

Then run the following program:

    f = open('alice.txt')
    print(f)
    text = f.read()
    print(text)
    columns = text.strip().split(';')
    print(columns)
    name = columns[0]
    age = int(columns[1])
    studies = columns[2]
    print(name)
    print(age)
    print(studies)

What happens?
