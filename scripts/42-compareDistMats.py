'''
prints the matrix for generated for linear on LR on LR data.
'''

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt
import scipy.stats

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816, 103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923, 106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123, 109325, 110411, 111312, 111413, 111514, 111716, 112819, 113215, 113619, 113821, 113922, 114419, 114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111, 120212, 120515, 121315, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422, 124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013, 130316, 130922, 131217, 131722, 131924, 132118, 133019, 133625, 133827, 133928, 134324, 135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231, 138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142424, 142626, 142828, 143325, 144226, 144832, 145531, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,
           103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,
           106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,
           109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419]

def loadData(fName):

	iFile =  csv.reader(open(fName, 'r'))
	abeMat = []

	for l in iFile:
		abeMat.append(l)
	abeMat = np.array(abeMat)
	abeMat = abeMat.astype(np.float)

	for i in range(len(abeMat)):
		for j in range(len(abeMat[i])):
			if abeMat[i][j] > 100 :
				abeMat[i][j] = np.float('nan')

	return abeMat

# 'abEmat_NL_LR_topRL.csv'

abeMat_NL_LR = loadData('abEmat_NL_LR_topRL.csv')
#abeMat_NL = loadData('abEmat_NL_LR.csv')
abeMat_NL = loadData('abEmat_L_LR-BC.csv')




for i in range(len(tasks)):
	print scipy.stats.mannwhitneyu(abeMat_NL[i * len(subjects):(i+1)* len(subjects), i * len(subjects):(i+1)* len(subjects)].flatten(), abeMat_NL_LR[i * len(subjects):(i+1)* len(subjects), i * len(subjects):(i+1)* len(subjects)].flatten())

