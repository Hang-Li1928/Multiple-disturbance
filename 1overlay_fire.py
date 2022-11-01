#  -*-coding:utf8 -*-
import os
import glob
import arcpy
import numpy as np
from arcpy.sa import *
from arcpy import env
env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
env.workspace = "F:\\test\\test\\temp"

a = []
aa = []
b = []
d = []

n = 0



buffer = "F:/test/test/temp_buffer.shp"
update = "F:/test/test/temp_buffer_addition.shp"
final = "F:/test/test/buffer_final.shp"

points = "F:\\test\\test\\combined_tree_ring.shp"
arcpy.Buffer_analysis(points, buffer, "1000 Meter")
arcpy.Update_analysis(buffer, "F:\\test\\test\\addition.shp", update, "BORDERS", "")

arcpy.Dissolve_management(update, final, "ORIG_FID", "", "MULTI_PART", "DISSOLVE_LINES")

for i in range(0, 241):
	arcpy.FeatureClassToFeatureClass_conversion(final, "F:/test/test","plot_" + str(i+1) + "p.shp", "ORIG_FID=" + str(i))


	
	
for i in range(1895,2018):
	
	
	all_fire = "F:\\test\\temp\\temp.shp"
	
	print i
	path = "F:\\test\\source\\fire_year\\%s\\*.shp" % i
	
	for fire in glob.glob(path): 
		a.append(fire)
		
		

		

	arcpy.Union_analysis(a, all_fire, "ALL", "", "GAPS")
	a = []
	
	temp1 = "F:/test/temp/fire_temp.shp"
	
	for  plot in glob.glob('F:/test/test/*p.shp'):
		print plot
		arcpy.Erase_analysis(plot, all_fire, temp1)

		
		
		arcpy.CalculateAreas_stats(temp1, "F:\\test\\temp\\temp1_cal.shp")
	
		cursor1 = arcpy.da.SearchCursor("F:\\test\\temp\\temp1_cal.shp", 'F_AREA')
		for row1 in cursor1:
			a.append(row1)
		ab = ''.join(str(a[0]))
		c= ab[1:-2]
		
	
		if float(c) < 3139000:  # S = π * r * r = 3.14 * 100 * 100 = 3140000   314000-1000 = 3139000 If the affected areas were larger than 1000 within the circle, we would define it as the affected plot
			d.append("1")       # If the plot was affected by the disturbance, we marked it as 1
			
			
		else:
					
			d.append("3")    # If the plot was  not affected by the disturbance, we marked it as 3
			
		
		a = []

		
		
with open("F:\\test\\test\\fire_ring.txt", 'w') as f:
	for line in d:
		f.write(line)
		
		if n == 240:
			f.write('\n')
			n = 0
		
		
		elif n < 240:
			f.write(',')
			n = n+ 1
f.close()
