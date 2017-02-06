
from collections import OrderedDict
# a dictionary that preserves insertion order


names = ["Adam", "Bea", "Charlie", "Danielle", "Eve", "Frantz", "Gustav", "Helena"]

od = OrderedDict()

for i, name in enumerate(names):
    od[i] = name

print(od)

od.move_to_end(2)
print(od)
