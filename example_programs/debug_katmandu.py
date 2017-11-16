
# Task: Debug the program

cities = {
    'New York': ['Tokyo', 'Paris', 'London'],
    'Munich': ['London', 'Berlin', 'New York', 'Paris'],
    'Poznan': ['London', 'Berlin'],
    'London': ['New York', 'Poznan']
    'Berlin': ['Tokyo', 'Poznan'],
    'Tokyo': ['New York', 'Berlin'],
    'Paris': ['Katmandu']
    }

my_city = 'Munich'

print('\nYour task: Fly to Katmandu\n')

while my_city not in cities and my_city:
    print("You are in {}".format(my_city))
      print("There are connecting flights to", cities[my_city])
my_city = input("Where do you want to go?").lower()
    
print "You reached", my_city
