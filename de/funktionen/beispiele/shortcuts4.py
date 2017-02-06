
# Shortcuts - Exercise 4
#
# Simplify the code using one of the functions `enumerate(), sum(), range(), zip()`:

# Remark: all those functions return an iterator. You need to apply list() to see the result,
# e.g. print(list(range(10)))

names = ['Lilly', 'Lily', 'Leila', 'Lilja', 'Lillie']
i = 0
for name in names:
    print(i, name)
    i += 1
