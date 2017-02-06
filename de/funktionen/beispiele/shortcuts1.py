
# Shortcuts - Exercise 1
#
# Simplify the code using one of the functions `enumerate(), sum(), range(), zip()`:

# Remark: all those functions return an iterator. You need to apply list() to see the result,
# e.g. print(list(range(10)))


counts = [356, 412, 127, 8, 32]

total = 0
for number in counts:
    total = total + number
print(total)
