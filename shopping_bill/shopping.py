
# program summing up items on a shopping bill.

items = {}
for line in open("bill.txt"):
    name, price = line.strip().split()
    price = int(price)
    if not name in items:
        items[name] = 0
    items[name] += price

data = []
for name, price in items.items():
    data.append( (price, name) )
data.sort()

print(data[-3:])


