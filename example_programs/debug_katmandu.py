
# Debug the program

cities = {
    'New York':['Tokyo','Paris','London'],
    'Poznan':['London','Berlin'],
    'London':['New York','Poznan']
    'Berlin':['Tokyo','Poznan'],
    'Tokyo':['New York','Berlin'],
    'Paris':['Katmandu']
    }

print

my_city = 'Poznan'

while not cities.has_key(my_city):
    print "You are in %s"%(my_city)
    print "Connecting flights to",cities[my_city]
    my_city = raw_input("Where do you want to go?").lower()
    
print "You reached", my_city
print
