
from operator import itemgetter

cities = [
          ('Poznan', 500000), 
          ('Berlin', 3200000), 
          ('Heidelberg', 50000), 
          ('London',9000000), 
          ('Dublin', 506000), 
          ('Warsaw', 1700000)
          ]
          
    
def print_cities(c):
    """Prints cities nicely."""
    for i, citydata in enumerate(c):
        name, population = citydata
        print("%3i. %-15s\t%10i"%(i+1, name, population))
    

print('\nunsorted:')
print_cities(cities)

print('\nsorted by name:')
cities.sort()
print_cities(cities)

print('\nsorted by population size:')
cities = sorted(cities, key=itemgetter(1))
print_cities(cities)

