
from operator import itemgetter

interfaces = [
        ['gig0/0.681', 681, 'VPN-1002', '171.26.192.100'],
        ['gig0/1.113', 113, 'VPN0113', None],
        ['gig0/1.114', 114, 'VPN0114', '10.50.53.57'],
        ['gig0/1.115', 115, 'VPN0115', '10.50.57.57'],
        ['gig0/1.116', 116, 'VPN0116', '10.50.61.57'],
]

column = 1
interfaces.sort(key=itemgetter(column))

for row in interfaces:
    print(row)

# TASK: what happens when you set column to 0, 1, 2, 3, 4 ?
# 
#       also try to set column to (1, 2)
  
