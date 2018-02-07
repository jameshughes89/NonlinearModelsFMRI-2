'''
prints the matrix for generated for linear on LR on LR data.
'''

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816, 103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923, 106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123, 109325, 110411, 111312, 111413, 111514, 111716, 112819, 113215, 113619, 113821, 113922, 114419, 114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111, 120212, 120515, 121315, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422, 124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013, 130316, 130922, 131217, 131722, 131924, 132118, 133019, 133625, 133827, 133928, 134324, 135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231, 138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142424, 142626, 142828, 143325, 144226, 144832, 145531, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,
           103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,
           106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,
           109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419]

def makePlot(iFile, title, pltz, c):

	iFile =  csv.reader(open(iFile, 'r'))
	abeMat = []
	for l in iFile:
		abeMat.append(l)
	abeMat = np.array(abeMat)
	abeMat = abeMat.astype(np.float)


	for i in range(len(abeMat)):
		for j in range(len(abeMat[i])):
			#abeMat[i][j] = log(abeMat[i][j])
			if abeMat[i][j] > 100 :
				abeMat[i][j] = np.float('nan')
				#abeMat[i][j] = np.float(1)



	avgMatTask = np.zeros((len(tasks),len(tasks)))

	for i in range(len(tasks)):
		for j in range(len(tasks)):
			avgMatTask[i,j] = np.nanmean(abeMat[i * len(subjects):(i+1)* len(subjects),j * len(subjects):(j+1)* len(subjects)])
	

	axes = plt.subplot2grid((1,4), (0, c))
	pltz.append(axes)
	im = pltz[c].matshow(avgMatTask, vmin=0.4, vmax=1.0)
	#plt.colorbar(label='Mean Absolute Error Averaged Over All Subjects')
	pltz[c].set_title(title)
	pltz[c].set_xlabel('Models')
	pltz[c].set_ylabel('Data')

	#if c == 0:
	pltz[c].set_yticks(range(7))
	pltz[c].set_yticklabels(["E", "G", "L", "M", "R", "S", "W"])
	#else:
	#	pltz[c].set_yticklabels([])	

	pltz[c].set_xticks(range(7))
	pltz[c].set_xticklabels(["E", "G", "L", "M", "R", "S", "W"])

	if c == 3:
		cbar_ax = fig.add_axes()
		fig.colorbar(im, cax=cbar_ax, label='Mean Absolute Error Averaged Over All Subjects')	

	for asd, cas in enumerate(avgMatTask):
		for sdf, c in enumerate(cas):
				plt.text(sdf-.4, asd+.2, "%.2f" % c)






pltz = []
fig = plt.figure(0)
makePlot('abEmat_NL_LR.csv', 'Nonlinear', pltz, 0)
#makePlot('abEmat_L_LR-BC.csv', 'BC', pltz, 1)
makePlot('abEmat_L_LR-BC_LASSO_1.csv', 'Linear: BC LASSO', pltz, 1)
#makePlot('abEmat_L_LR-FDR.csv', 'FDR', pltz, 3)
makePlot('abEmat_L_LR-FDR_LASSO_1.csv', 'Linear: FDR LASSO', pltz, 2)
#makePlot('abEmat_L_LR-TOP30.csv', 'ALL', pltz, 5)
makePlot('abEmat_L_LR-TOP30_LASSO_1.csv', 'Linear: LASSO', pltz, 3)

plt.show()





