
# Warming up

Execute the following program. Explain what happens.

    names = ['Adam', 'Bob', 'Charlie']

    f = open('boy_names.txt', 'w')
    for name in names:
        f.write(name + '\n')
    f.close()

Remove the `+ '\n'` from the code and run the program again. What happens?
