"""
Schreiben einer Textdatei:
1. Oeffnen mit open() und 'w' (overwrite) oder 'a' (append)
2. Strings mit write() in die Datei schreiben
3. Datei mit close() am Ende schliessen
"""

cities = [
          ('Poznan', 500000), 
          ('Berlin', 3200000), 
          ('Heidelberg', 50000), 
          ('London',9000000), 
          ('Dublin', 506000), 
          ('Warsaw', 1700000)
          ]
          
with open('cities.csv', 'w') as f:
    for city, pop in cities:
        line = "{}\t{}".format(city, pop)
        f.write(line)
