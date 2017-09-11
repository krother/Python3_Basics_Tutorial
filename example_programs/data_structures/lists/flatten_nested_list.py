
# make a simple list out of the data

data = [
    [ 0, 1, 2, 3],
    [10,11,12,13],
    [20,21,22,23]
    ]

# SOLUTION 1:

def flatten1(data):
    result = []
    for row in data:
        for cell in row:
            result.append(cell)
    return result

# SOLUTION 2:

def flatten2(seq):
    for item in seq:
        if isinstance(item, list):
            for subitem in flatten2(item):
                yield subitem
        else:
            yield item

print(flatten1(data))
print(list(flatten2(data)))

# SOLUTION 3:
from itertools import chain
print(list(chain(*data)))


        

