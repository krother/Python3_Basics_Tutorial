
# Example: representing data as a table

#
# 1. Lists in a list, horizontally
#
cities1 = [
          ['Poznan', 500000], 
          ['Berlin', 3200000], 
          ['Heidelberg', 50000], 
          ['London',9000000], 
          ['Dublin', 506000], 
          ['Warsaw', 1700000]
          ]


#
# 2. Lists in a list, vertically
#
cities2 = [
    ['Poznan', 'Berlin', 'Heidelberg', 'London', 'Dublin', 'Warsaw'],
    [500000, 3200000, 50000, 9000000, 506000, 1700000],
    ]


#
# 3. Simple dictionary
#

cities3 = {
          'Poznan':500000, 
          'Berlin':3200000, 
          'Heidelberg':50000,
          'London':9000000,
          'Dublin':506000,
          'Warsaw':1700000
          }
    

#
# 4. Lists in a dictionary (keys as column labels)
#
cities4 = {
    'names':['Poznan', 'Berlin', 'Heidelberg', 'London', 'Dublin', 'Warsaw'],
    'populations':[500000, 3200000, 50000, 9000000, 506000, 1700000],
    }


#
# 5. Dictionaries in a list
#
cities5 = [
          {'name':'Poznan',     'population':500000}, 
          {'name':'Berlin',     'population':3200000}, 
          {'name':'Heidelberg', 'population':50000}, 
          {'name':'London',     'population':9000000}, 
          {'name':'Dublin',     'population':506000}, 
          {'name':'Warsaw',     'population':1700000}
          ]


#
# 6. dictionary in a dictionary
#
cities6 = {
          'Poznan':{'population':500000}, 
          'Berlin':{'population':3200000}, 
          'Heidelberg':{'population':50000}, 
          'London':{'population':9000000}, 
          'Dublin':{'population':506000}, 
          'Warsaw':{'population':1700000}
          }

#
# Exercise: 
# 1) Add a new city to each of the tables
# 2) Print one of the cities with its population.
#
