
# 1. Using dictionaries as records.
person = {
          'name': "Mike Miller", 
          'born':1968, 
          'email':'mike@miller.com', 
          'height':1.71
          }

person2 = {
           'name': "Asia Ilska",
           'born':1985,
           'email':'asia@o2.pl',
           'height':1.64
          }

person_dict = {'Miller':person,'Ilska':person2}        

for p in person_dict.values():
    pass
#   print p
#   print "%s is %4.2f meters tall."%(p['name'], p['height'])


#
# 2. Using tuples as records.
#
person = ("Mike Miller", 1968, 'mike@miller.com', 1.71)
person2 = ("Asia Ilska", 1985, 'asia@o2.pl', 1.64)

person_list = [person, person2]

for p in person_list:
    print p
    print "%s is %4.2f meters tall."%(p[0], p[3])

# Exercise: What are advantages and disadvantages of both methods?
