
# Example: reading a text file

cities = []

for line in open('cities.csv'):
    columns = line.split(',')
    name = columns[0]
    size = int(columns[1])
    cities.append( (name, size) )

    


