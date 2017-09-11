
# Example: calculate a linear regression from a table

# Data taken from Lowry 1951, the most cited publication of all time.

table = [
    ['protein', 'ext1', 'ext2', 'ext3'],
    [0.16, 0.038, 0.044, 0.040],
    [0.33, 0.089, 0.095, 0.091],
    [0.66, 0.184, 0.191, 0.191],
    [1.00, 0.280, 0.292, 0.283],
    [1.32, 0.365, 0.367, 0.365],
    [1.66, 0.441, 0.443, 0.444]
    ]

# remove the line with labels
table = table[1:] 

protein, ext1, ext2, ext3 = zip(*table)

# put three columns
protein = protein * 3
extinction = ext1 + ext2 + ext3

table = zip(protein, extinction)

# calculate the linear regression
av_pro = sum(protein) / len(protein)
av_ext = sum(extinction) / len(extinction)

product1 = [(e - av_ext) * (av_pro - p) for p, e in table]
product2 = [(av_pro - p) ** 2 for p in protein]

slope = -sum(product1) / sum(product2)
xoffset = av_ext - slope * av_pro

e = float(raw_input('Enter extinction: '))
print 'protein concentration', (e - xoffset) / slope
