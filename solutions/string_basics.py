# Manipulating strings

# fill in the gaps

a = "With 4 parameters I can fit an elephant"

b = a.upper()
assert b == "WITH 4 PARAMETERS I CAN FIT AN ELEPHANT"

c = a.replace('elephant', 'alligator')
assert c == "With 4 parameters I can fit an alligator"

d = a[18:]
assert d == "I can fit an elephant"

e = d.split()
assert e == ['I', 'can', 'fit', 'an', 'elephant']

f = '***'.join(e)
assert f == "I***can***fit***an***elephant"

g = ' '.join([e[-1]] * 3)
assert g == 'elephant elephant elephant'

h = a.find('elephant')
assert h == 31

i = a.count('e')
assert i == 4

j = a + " and with 5 it will wiggle its trunk."
assert j.endswith("and with 5 it will wiggle its trunk.")
