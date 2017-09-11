'''
read a series of numbers from a text file
and print a summary of the data
'''

data = []

for line in open('neuron_data.txt'):
    length = float(line.strip())
    data.append(length)

n_items = len(data)
total = sum(data)
shortest = min(data)
longest = max(data)

data.sort()

output = open("results.txt","w")
output.write("number of dendritic lengths : %4i \n"%(n_items))
output.write("total dendritic length      : %6.1f \n"%(total))
output.write("shortest dendritic length   : %1.2f \n"%(shortest))
output.write("longest dendritic length    : %7.2f \n"%(longest))
output.write("%34.2f\n%34.2f"%(data[-2], data[-3]))
output.close()neuron_length
