# Format Strings
label = "knights"
n = 12  # number by John Dryden, not Monty Python
mean = 1.2345678

# produce the following strings using the data from the variables
str(n)
"12"

# format string: >= 3.5
f"{label}: {n}"
template = "{}: {}"
template.format(label, n)

str(label) + ': ' + str(n)
"%s: %i" % (label, n)

"knights: 12"

"{}: {}".format(label.upper()[:3], n)
"KNI: 12"

f"There are {n} {label} of the table round"
"There are 12 knights of the table round"

print(f"{label}\t\t:\t{n}")
f"{label:10}:{n:10}"
"knights   :    12"

f"{label:>10}:{n:<10}"
"   knights:    12"

f"{label:10}:{n:010d}"
"knights   : 00012"


print(f"{label}\n{n}\n{mean}")
data = ['knights', '12', '12345']
print('\n'.join(data))
"""knights
12
1.2345678"""

str(round(mean, 2))
f"{mean:.2f}"
"1.23"   1.

f"{mean:15.10f}"
"  1.2345678000"



print(f"{n}")
print(f"{label}: {n}")
print(f"{label[:3].upper()}: {n}")
print(f"There are {n} {label} of the table round")
print(f"{label:10}: {n:5}")
print(f"{label:>10}: {n:5}")
print(f"{label:10}: {n:05}")
print(f"{label}\n{n}\n{mean}")
print(f"{mean:4.2f}")
print(f"{mean:14.10f}")
