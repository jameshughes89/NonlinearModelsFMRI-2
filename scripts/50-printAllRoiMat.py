

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt


#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,
           103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,
           106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,
           109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419]

def makePlot(iFile, title, pltz, c):

	roiMat = []
	for l in iFile:
		roiMat.append(l)
	roiMat = np.array(roiMat)
	roiMat = roiMat.astype(np.float)

	axes = plt.subplot2grid((4,1), (c, 0))
	pltz.append(axes)
	#pltz[c].set_title(title)

	#_#_#_#_#_#

	cmap = plt.get_cmap(lut=np.nanmax(roiMat)-np.nanmin(roiMat)+1)
	pltz[c].matshow(roiMat, aspect='auto', cmap=cmap, vmin=0, vmax=40)
	#pltz[c].colorbar(label='Count')
	if c == 3:	
		pltz[c].set_xlabel('ROI')
	pltz[c].set_ylabel(title)


	if c == 0:
		pltz[c].set_xticks(range(30))
		pltz[c].set_xticklabels(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"])
	else:
		pltz[c].set_xticklabels([])	

	pltz[c].set_yticks(range(7))
	pltz[c].set_yticklabels(["E", "G", "L", "M", "R", "S", "W"], rotation =90)

	for asd, cas in enumerate(roiMat):
		for sdf, c in enumerate(cas):
				plt.text(sdf-.4, asd+.2, int(c), fontsize=8)

	#plt.show()

pltz = []

iFile =  csv.reader(open('roiCount_NL.csv', 'r'))
makePlot(iFile, 'Nonlinear', pltz, 0)
iFile =  csv.reader(open('roiCount_BC_Lasso.csv', 'r'))
makePlot(iFile, 'Linear BC LASSO', pltz, 1)
iFile =  csv.reader(open('roiCount_FDR_Lasso.csv', 'r'))
makePlot(iFile, 'Linear FDR LASSO', pltz, 2)
#iFile =  csv.reader(open('roiCount_BC.csv', 'r'))
#makePlot(iFile, 'Linear BC', pltz, 1)
#iFile =  csv.reader(open('roiCount_FDR.csv', 'r'))
#makePlot(iFile, 'Linear FDR', pltz, 2)
iFile =  csv.reader(open('roiCount_TOP_Lasso.csv', 'r'))
makePlot(iFile, 'Linear LASSO', pltz, 3)

plt.suptitle('ROI Counts From All Subjects on All Tasks for Multiple Model Types')
plt.show()





