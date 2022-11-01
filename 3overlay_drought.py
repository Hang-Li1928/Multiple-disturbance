import os
import numpy as np



f = open(r"F:\\test\\source\\drought_year\\PDSI_combination_new.txt")
line = f.readline()
data = np.zeros((123,241))#this is the row and line
i = 0

while line:
	num = np.array([float(x) for x in line.split("\t")])
	data[i,:] = num
	line = f.readline()
	i = i+1
f.close


i = 0
for j in range(0,241):

  	for i in range(0,123): 
		if data[i,j] >  -1.5:  # normal year
			data[i,j]=3
		elif data[i,j] <= -1.5 and data[i,j] > -5: # mild dry year
			data[i,j] = 2
		elif data[i,j] <= -1.5: # extreme dry year
			data[i,j]=1

with open("F:\\test\\test\\drought_ring.txt", 'w') as outfile: 
    for row in data: 
     outfile.write(','.join([str(num) for num in row])) 
     outfile.write('\n') 
	 
outfile.close	



