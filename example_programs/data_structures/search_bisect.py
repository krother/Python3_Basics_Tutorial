
# searching elements in a list:

# based on cookbook 5.9
import random
import bisect

numbers = range(22)
data = [random.choice(numbers) for i in range(100)]

data.sort()
print data

# if list is unsorted:
if 20 in data:
    print '20 present'
    print data.index(20)
    # SLOW!

# if list is sorted - use binary tree

index = bisect.bisect_right(data, 20) -1
present = data[index] == 20
if present:
    print '20 present'
    print index
    
