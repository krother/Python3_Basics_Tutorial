

data = [
    [ 0, 1, 2, 3],
    [10,11,12,13],
    [20,21,22,23]
    ]

# print all columns of the table
for col in zip(*data):
    print(col)

    
# exchange rows and columns in a 2D table

print([list(col) for col in zip(*data)])


