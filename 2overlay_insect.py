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
	
	
	all_insect = "F:\\test\\temp\\temp.shp"
	
	print i
	path = "F:\\test\\source\\insect_year\\%s\\*.shp" % i
	
	for insect in glob.glob(path): 
		a.append(insect)
		
		

		

	arcpy.Union_analysis(a, all_insect, "ALL", "", "GAPS")
	a = []
	
	temp1 = "F:/test/temp/insect_temp.shp"
	
	for  plot in glob.glob('F:/test/test/*p.shp'):
		print plot
		arcpy.Erase_analysis(plot, all_insect, temp1)

		
		
		arcpy.CalculateAreas_stats(temp1, "F:\\test\\temp\\temp1_cal.shp")
	
		cursor1 = arcpy.da.SearchCursor("F:\\test\\temp\\temp1_cal.shp", 'F_AREA')
		for row1 in cursor1:
			a.append(row1)
		ab = ''.join(str(a[0]))
		c= ab[1:-2]
		
		
	
		if float(c) < 3139000: 
			d.append("1")
			
			
		else: #no sure
					
			d.append("3")
			
		
		a = []

		
		
with open("F:\\test\\test\\insect_ring.txt", 'w') as f:
	for line in d:
		f.write(line)
		
		if n == 240:
			f.write('\n')
			n = 0
		
		
		elif n < 240:
			f.write(',')
			n = n+ 1
f.close()
