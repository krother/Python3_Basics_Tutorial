"""
Convert a dictionary to a nested list 
and vice versa.

This code example is more explicit,
allows more control on the order of columns,
but contains more code.
"""

d = {'Sci-Fi': 25882, 'Crime': 38988, 'Romance': 55930, 
     'Animation': 47234, 'Music': 34482, 'Adult': 62763, 
     'Comedy': 211680, 'War': 13409, 'Horror': 39490, 
     'Commercial': 1, 'Film-Noir': 583, 'Adventure': 33337, 
     'News': 8663, 'Erotica': 1, 'Reality-TV': 11119, 
     'Thriller': 53856, 'Western': 14048, 'Mystery': 24829, 
     'Short': 430403, 'Lifestyle': 1, 'Talk-Show': 7784, 
     'Drama': 288422, 'Action': 55047, 'Documentary': 164431, 
     'Musical': 15269, 'Experimental': 1, 'History': 17167, 
     'Family': 44130, 'Fantasy': 29331, 'Game-Show': 4596, 
     'Sport': 16978, 'Biography': 19719
     }

# create nested list
tab = []
for key in d.keys():
    zeile = [ d[key], key ] 
    tab.append(zeile)
print(tab)

# print highest number
tab.sort()
print(tab[-1])

# convert table back to a dictionary
e = {}
for zeile in tab:
    e[ zeile[1] ] = zeile[0]
print(e)
