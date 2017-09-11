
connections = {
    'New York':['Tokyo','Paris','London'],
    'Poznan':['London','Berlin'],
    'London':['New York','Poznan'],
    'Berlin':['Tokyo','Poznan'],
    'Tokyo':['New York','Berlin'],
    'Paris':['Katmandu'], 
    'Katmandu':[]
    }

print 'Please fly to Katmandu.'

my_city = 'Poznan'

while my_city != 'Katmandu':
    print
    print "You are in %s"%(my_city)
    print "Connecting flights to", connections[my_city]
    new_city = raw_input("Where do you want to go? ")
    
    if connections.has_key(new_city) and new_city in connections[my_city]:
        my_city = new_city
    else:
        print "You cannot fly to %s."%new_city

print "\nYou reached", my_city
print
