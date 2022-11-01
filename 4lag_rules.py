import os
import numpy as np

# Drought lag (0 Year)
f = open(r"F:\\test\\test\\drought_ring.txt")
line = f.readline()
data = np.zeros((123,241))#this is the row and line
i = 0

while line:
	num = np.array([float(x) for x in line.split(",")])
	data[i,:] = num
	line = f.readline()
	i = i+1
f.close

			
with open("F:\\test\\test\\drought_lag.txt", 'w') as outfile: 
    for row in data: 
     outfile.write(' '.join([str(num) for num in row])) 
     outfile.write('\n') 
	 
outfile.close	 
	 

	 

	 
# Fire lag (4 Year)	 

f = open(r"F:\\test\\test\\fire_ring.txt")
line = f.readline()
data = np.zeros((123,241))#this is the row and line
data2 = np.zeros((123,241))
i = 0

while line:
	num = np.array([float(x) for x in line.split(",")])
	data[i,:] = num
	line = f.readline()
	i = i+1
f.close

data2 = data

i = 0  #It is the rules that if in one year the tree has been influenced by fire, the influences will last the next four years 
for j in range(0,241): # this is the line

		
  	for i in range(121,-1,-1): 
		
		if i == 120 and data[i,j]==1: # this is the second last
			data[i+1,j]=1
		
		
		if i == 119 and data[i,j]==1: # this is the third last
			data[i+1,j]=1
			data[i+2,j]=1
			
		if i == 118 and data[i,j]==1: # this is the fourth last
			data[i+1,j]=1
			data[i+2,j]=1
			data[i+3,j]=1
			
			
		elif i < 118 and data[i,j]==1: # this is the fifth last
			data[i+1,j]=1
			data[i+2,j]=1
			data[i+3,j]=1
			data[i+4,j]=1
			
	

with open("F:\\test\\test\\fire_lag.txt", 'w') as outfile: 
    for row in data: 
     outfile.write(' '.join([str(num) for num in row])) 
     outfile.write('\n') 
	 
outfile.close







# Insect lag (4 Year)

f = open(r"F:\\test\\test\\insect_ring.txt")
line = f.readline()
data = np.zeros((123,241))#this is the row and line
i = 0

while line:
	num = np.array([float(x) for x in line.split(",")])
	data[i,:] = num
	line = f.readline()
	i = i+1
f.close

i = 0  #It is the rules that if in one year the tree has been invaded by insect, the influences will last the next four years 
for j in range(0,241): # this is the line

		
  	for i in range(121,-1,-1): 
		
		if i == 120 and data[i,j]==1: # this is the second last
			data[i+1,j]=1
		
		
		if i == 119 and data[i,j]==1: # this is the third last
			data[i+1,j]=1
			data[i+2,j]=1
			
		if i == 118 and data[i,j]==1: # this is the fourth last
			data[i+1,j]=1
			data[i+2,j]=1
			data[i+3,j]=1
			
			
		elif i < 118 and data[i,j]==1: # this is the fifth last
			data[i+1,j]=1
			data[i+2,j]=1
			data[i+3,j]=1
			data[i+4,j]=1
	

with open("F:\\test\\test\\insect_lag.txt", 'w') as outfile: 
    for row in data: 
     outfile.write(' '.join([str(num) for num in row])) 
     outfile.write('\n') 
	 
outfile.close	