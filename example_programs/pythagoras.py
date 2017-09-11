
print "Find out whether a triangle is straight-edged."

a = float(input("length of edge a: "))
b = float(input("length of edge b: "))
c = float(input("length of edge c: "))

if a ** 2 + b ** 2  == c ** 2:
    print "This is a straight-edged triangle." 
else:
    print "This is not a straight-edged triangle." 

