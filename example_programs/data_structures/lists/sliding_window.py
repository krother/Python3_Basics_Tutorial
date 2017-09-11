
# sliding window algorithm / n-grams

# based on Cookbook 19.7 - modified


# simple case
def slicing(data, length=2):
    result = data[:length]
    offset = length
    while len(result) == length:
        yield result
        result = result[length:] + data[offset:offset+length]
        offset += length
    if result:
        yield result

# more complex - n-grams
def sliding_window(data, length=2, overlap=0):
    result = data[:length]
    shift = length-overlap
    offset = shift
    while len(result) == length:
        yield result
        result = result[shift:] + data[offset:offset+shift]
        offset += shift
    if result:
        yield result

#TODO: check usage of itertools!

seq = "THISISNQTAPRQTEINSEQWENCE"

print list(sliding_window(seq, 4, 0))

print list(sliding_window(seq, 5, 4))
