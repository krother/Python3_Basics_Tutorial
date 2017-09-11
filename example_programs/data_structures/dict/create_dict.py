
# create a dictionary from a tuple (or list)

data = ("Mike Madison", 1977, "programmer")
labels = ["name","year","job"]

record = dict(zip(labels, data))
print record

# convert back again
plain = [record[k] for k in labels]
print plain

# reverse keys and values in a dictionary
# cookbook 4.14
reverse = dict([(v,k) for k,v in record.items()])
print reverse

