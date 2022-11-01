import os
import numpy as np

# f = fire; i = insect, d = drought
f_i_d_m = [] # the selected tree rings for fire_insect_moderate_drought
f_i_d_e = [] # the selected tree rings for fire_insect_extreme_drought

f_i = [] # the selected tree rings for fire_insect

f_d_m = [] # the selected tree rings for fire_moderate_drought
f_d_e = [] # the selected tree rings for fire_extreme_drought

i_d_m = [] # the selected tree rings for insect_moderate_drought
i_d_e = [] # the selected tree rings for insect_extreme_drought


fire = [] # the selected tree rings for fire

insect = [] # the selected tree rings for insect

drought_m = [] # the selected tree rings for moderate_drought
drought_e = [] # the selected tree rings for extreme_drought

control = [] # the selected tree rings for control group




# PDSI for each disturbance combination will also be calculated.

PDSI_f_i_d_m = [] #PDSI for fire_insect_moderate_drought
PDSI_f_i_d_e = [] #PDSI for fire_insect_extreme_drought
 
PDSI_f_i = [] #PDSI for fire_insect

PDSI_f_d_m = [] #PDSI for fire_moderate_drought
PDSI_f_d_e = [] #PDSI for fire_extreme_drought


PDSI_i_d_m = [] #PDSI for insect_moderate_drought
PDSI_i_d_e = [] #PDSI for insect_extreme_drought

PDSI_fire = [] #PDSI for fire

PDSI_insect = [] #PDSI for insect

PDSI_drought_m = [] #PDSI for moderate drought
PDSI_drought_e = [] #PDSI for extreme drought

PDSI_control = [] # PDSI for control group


#input the drought data

f_drought = open(r"F:\\test\\test\\drought_lag.txt")
line = f_drought.readline()
data_drought = np.zeros((123,241))#this is the row and line
i = 0

while line:
	num = np.array([float(x) for x in line.split(" ")])
	data_drought[i,:] = num
	line = f_drought.readline()
	i = i+1
f_drought.close


#input the fire data

f_fire = open(r"F:\\test\\test\\fire_lag.txt")
line = f_fire.readline()
data_fire = np.zeros((123,241))#this is the row and line
i = 0

while line:
	num = np.array([float(x) for x in line.split(" ")])
	data_fire[i,:] = num
	line = f_fire.readline()
	i = i+1
f_fire.close


#input the insect data

f_insect = open(r"F:\\test\\test\\insect_lag.txt")
line = f_insect.readline()
data_insect = np.zeros((123,241))#this is the row and line
i = 0

while line:
	num = np.array([float(x) for x in line.split(" ")])
	data_insect[i,:] = num
	line = f_insect.readline()
	i = i+1
f_insect.close


#input the tree ring data

f_ring = open(r"F:\\test\\source\\tree ring\\TRW_all_test.csv")  
line = f_ring.readline()
data_ring = np.zeros((123,241))#this is the row and line
i = 0

while line:
	
	num = np.array([float(x) for x in line.split(",")])
	data_ring[i,:] = num
	line = f_ring.readline()
	i = i+1
f_ring.close


#input the PDSI data

f_pdsi = open(r"F:\\test\\source\\drought_year\\PDSI_combination_new.csv")
line = f_pdsi.readline()
data_pdsi = np.zeros((123,241))#this is the row and line
i = 0

while line:
	
	num = np.array([float(x) for x in line.split(",")])
	data_pdsi[i,:] = num
	line = f_pdsi.readline()
	i = i+1
f_pdsi.close



i = 0
for i in range(0,123): 
  	for j in range(0,241): 

		
		if data_drought[i,j]==1 and data_fire[i,j]==1 and data_insect[i,j]==1 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			f_i_d_e.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_f_i_d_e.append(m)
			
		elif data_drought[i,j]==2 and data_fire[i,j]==1 and data_insect[i,j]==1 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			f_i_d_m.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_f_i_d_m.append(m)
			
			
			
			
			
		elif data_drought[i,j]==3 and data_fire[i,j]==1 and data_insect[i,j]==1 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			f_i.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_f_i.append(m)
			
			
			
			
			
		elif data_drought[i,j]==1 and data_fire[i,j]==3 and data_insect[i,j]==1 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			i_d_e.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_i_d_e.append(m)
		
		elif data_drought[i,j]==2 and data_fire[i,j]==3 and data_insect[i,j]==1 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			i_d_m.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_i_d_m.append(m)


			
			
		
		elif data_drought[i,j]==1 and data_fire[i,j]==1 and data_insect[i,j]==3 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			f_d_e.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_f_d_e.append(m)
		
		elif data_drought[i,j]==2 and data_fire[i,j]==1 and data_insect[i,j]==3 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			f_d_m.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_f_d_m.append(m)

		
			
			
			
			
		elif data_drought[i,j]==3 and data_fire[i,j]==1 and data_insect[i,j]==3 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			fire.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_fire.append(m)
			
			
			
			
			
		elif data_drought[i,j]==3 and data_fire[i,j]==3 and data_insect[i,j]==1 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			insect.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_insect.append(m)
			


			
			
		elif data_drought[i,j]==1 and data_fire[i,j]==3 and data_insect[i,j]==3 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			drought_e.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_drought_e.append(m)
			
		elif data_drought[i,j]==2 and data_fire[i,j]==3 and data_insect[i,j]==3 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			drought_m.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_drought_m.append(m)	
			
			
			
			
		elif data_drought[i,j]==3 and data_fire[i,j]==3 and data_insect[i,j]==3 and data_ring[i,j]!=99999.0:
			n = str(data_ring[i,j])
			control.append(n)
			
			m = str(data_pdsi[i,j])
			PDSI_control.append(m)
		n=0	
		m=0
	


	
n=0
m=0
with open('F:\\test\\result\\mul_f_i_d_e.txt', 'w') as f:
	for line in f_i_d_e:
		f.write(line)
		f.write(',')
f.close()	 

with open('F:\\test\\result\\mul_f_i_d_m.txt', 'w') as f:
	for line in f_i_d_m:
		f.write(line)
		f.write(',')
f.close()	





n=0
with open('F:\\test\\result\\mul_i_d_e.txt', 'w') as f:
	for line in i_d_e:
		f.write(line)
		f.write(',')
f.close()

n=0
with open('F:\\test\\result\\mul_i_d_m.txt', 'w') as f:
	for line in i_d_m:
		f.write(line)
		f.write(',')
f.close()





n=0
with open('F:\\test\\result\\mul_f_d_e.txt', 'w') as f:
	for line in f_d_e:
		f.write(line)
		f.write(',')
f.close()

n=0
with open('F:\\test\\result\\mul_f_d_m.txt', 'w') as f:
	for line in f_d_m:
		f.write(line)
		f.write(',')
f.close()





n=0
with open('F:\\test\\result\\mul_f_i.txt', 'w') as f:
	for line in f_i:
		f.write(line)
		f.write(',')
f.close()








n=0
with open('F:\\test\\result\\mul_f.txt', 'w') as f:
	for line in fire:
		f.write(line)
		f.write(',')

f.close()







n=0
with open('F:\\test\\result\\mul_i.txt', 'w') as f:
	for line in insect:
		f.write(line)
		f.write(',')

f.close()






n=0
with open('F:\\test\\result\\mul_d_e.txt', 'w') as f:
	for line in drought_e:
		f.write(line)
		f.write(',')
f.close()

n=0
with open('F:\\test\\result\\mul_d_m.txt', 'w') as f:
	for line in drought_m:
		f.write(line)
		f.write(',')
f.close()	




	
n=0
with open('F:\\test\\result\\mul_control.txt', 'w') as f:
	for line in control:
		f.write(line)
		f.write(',')

f.close()






# calculate the all PDSI values for each combination
n=0
with open('F:\\test\\result\\PDSI_f_i_d_e.txt', 'w') as f:
	for line in PDSI_f_i_d_e:
		f.write(line)
		f.write(',')
f.close()

n=0
with open('F:\\test\\result\\PDSI_f_i_d_m.txt', 'w') as f:
	for line in PDSI_f_i_d_m:
		f.write(line)
		f.write(',')
f.close()






n=0
with open('F:\\test\\result\\PDSI_f_i.txt', 'w') as f:
	for line in PDSI_f_i:
		f.write(line)
		f.write(',')
f.close()





n=0
with open('F:\\test\\result\\PDSI_f_d_e.txt', 'w') as f:
	for line in PDSI_f_d_e:
		f.write(line)
		f.write(',')
f.close()

n=0
with open('F:\\test\\result\\PDSI_f_d_m.txt', 'w') as f:
	for line in PDSI_f_d_m:
		f.write(line)
		f.write(',')
f.close()







n=0
with open('F:\\test\\result\\PDSI_i_d_e.txt', 'w') as f:
	for line in PDSI_i_d_e:
		f.write(line)
		f.write(',')
f.close()

n=0
with open('F:\\test\\result\\PDSI_i_d_m.txt', 'w') as f:
	for line in PDSI_i_d_m:
		f.write(line)
		f.write(',')
f.close()






n=0
with open('F:\\test\\result\\PDSI_fire.txt', 'w') as f:
	for line in PDSI_fire:
		f.write(line)
		f.write(',')
f.close()





n=0
with open('F:\\test\\result\\PDSI_insect.txt', 'w') as f:
	for line in PDSI_insect:
		f.write(line)
		f.write(',')
f.close()





n=0
with open('F:\\test\\result\\PDSI_drought_e.txt', 'w') as f:
	for line in PDSI_drought_e:
		f.write(line)
		f.write(',')
f.close()

n=0
with open('F:\\test\\result\\PDSI_drought_m.txt', 'w') as f:
	for line in PDSI_drought_m:
		f.write(line)
		f.write(',')
f.close()




n=0
with open('F:\\test\\result\\PDSI_control.txt', 'w') as f:
	for line in PDSI_control:
		f.write(line)
		f.write(',')
f.close()