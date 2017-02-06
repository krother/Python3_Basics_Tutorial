
# Shortcuts - Exercise 3
#
# Simplify the code using one of the functions `enumerate(), sum(), range(), zip()`:

# Remark: all those functions return an iterator. You need to apply list() to see the result,
# e.g. print(list(range(10)))


names = ['Lilly', 'Lily', 'Leila', 'Lilja', 'Lillie']
counts = [356, 412, 127, 8, 32]
table = []
i = 0
while i < len(names):
    row = (names[i], counts[i])
    table.append(row)
    i += 1
print(table)
