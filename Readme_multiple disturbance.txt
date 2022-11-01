
The file is based on Multiple disturbance paper written by Li et al. Some detailed process can be found in the Python comments or our paper. If you have more questions about the code, you are welcomed to contact me via email: lihang192800@gmail.com 




Prerequisite: Before you run the codes, you need to have the following:

Your computer should have at least 6GB RAM. You should have Python 2.7 and Arcmap (The version should be higher than 10.4).




The file has 4 folders. 

The first fold is the "source" which contain drought(PDSI for each plots from 1895 to 2017), fire (shapefiles from 1895 to 2017),and insect (shapefiles from 1895 to 2017). It also contains the tree-ring indices for each chronology.

The second fold is the "test" where the coding may generate some temperary documents or some unimportant results.

The third folder is the "result" where the coding may generate some important results or some well-processed results by me.

The fourth fold is the "code" which includes all the codes. 



The process of the research:

1. Disturbance detection (fire, insect and drought)
	1.1 The python will detect fire for each chronology from 1895 to 2017. The number of total detection reaches 241 * (2017- 1895+1) = 29643. It may take a long time, more than 12 hours with a normal computer. You should be very patient.


	1.2 The python will detect insect for each chronology from 1895 to 2017. The number of total detection reaches 241 * (2017- 1895+1) = 29643. It may take a long time, more than 12 hours with a normal computer. You should be very patient.


       1.3 According the machine order* (I will explain what the machine order later), you should reorganize the chronology order and then detect drought for each chronology from 1895 to 2017 according to our drought definition. It may take less than 2 mins. 



2. Lag Effect
	The disturbances have some lag effects on the further growing in the following years. The code considers the lag effects.


3. Diving all rings into 8 subgroups
	The code will generate a PDSI and a tree-ring index txt file for each disturbance combination. You just need to drag them into the excel, like the result excel document and calculate the average values for each subgroups     