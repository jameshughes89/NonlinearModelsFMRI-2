'''
Creates my fun p-value transition plots. 

'''

import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 50}

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
topXs = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]


allNL = []
allL = []
for t in tasks:
	print t

	iFile = csv.reader(open('./topModels/bestExpressionsError-NL-' + t +'.txt','r'))
	NL = []
	for l in iFile:
		NL.append(float(l[0]))
	NL = np.array(NL)
	allNL.append(NL)

	L = []
	for i in topXs:
		iFile = csv.reader(open('./topModels/bestExpressionsError-L-TOP' + str(i) + '-' + t +'.txt','r'))
		TOPX = []
		count = 0				# makes sure there are the same number of subjects loaded. 
		for l in iFile:
			TOPX.append(float(l[0]))
			count +=1
			if count == allNL[0].shape[0]:		# NOTE: This bit makes sure it's same number of subjects being compared 
				break							# Comment out if you don't want for whatever reason
		TOPX = np.array(TOPX)
		L.append(TOPX)

	allL.append(L)
	

line = " & "
for j in range(len(tasks)):
	line = line + str(tasks[j])
	if j != len(tasks)-1:
		line = line + ' & '

print line

line = " & "
for j in range(len(tasks)):
	line = line + ("%.3f" % round(np.mean(allNL[j]), 3)) + ' & ' + ("%.3f" % round(np.std(allNL[j]), 3)) + ' & & '

print line

pVals = np.zeros((len(topXs), len(tasks)))

for i in range(len(topXs)):
	line = str(topXs[i]) + ' & '
	for j in range(len(tasks)):
		line = line + ("%.3f" % round(np.mean(allL[j][i]), 3)) + ' & ' 
		line = line + ("%.3f" % round(np.std(allL[j][i]), 3)) + ' & ' 
		line = line + ("%.3f" % round(sts.mannwhitneyu(allNL[j], allL[j][i]).pvalue, 3))
		pVals[i][j] = sts.mannwhitneyu(allNL[j], allL[j][i]).pvalue
		if j != len(tasks)-1:
			line = line + ' & '

	print line


plt.matshow(pVals, aspect='auto')
plt.title('Probability Value Transition Plot')
plt.xlabel('Task')
plt.xticks(range(len(tasks)), ["E", "G", "L", "M", "R", "S", "W"])
plt.ylabel('Number of ROI --- DF + 1')
plt.yticks(range(len(topXs)), topXs)
plt.colorbar(label='p-value (Mann-Whitney U Test)')


# # #
# Font was 20
# # #

#NL TOP
plt.text(0 - 0.3, 7.95 + 0.2 - 2, 'NL-A-7.95', fontsize=10, color='w')
plt.text(1 - 0.3, 8.30 + 0.2 - 2, 'NL-A-8.30', fontsize=10, color='w')
plt.text(2 - 0.3, 9.65 + 0.2 - 2, 'NL-A-9.65', fontsize=10, color='w')
plt.text(3 - 0.3, 9.29 + 0.2 - 2, 'NL-A-9.29', fontsize=10, color='w')
plt.text(4 - 0.3, 8.61 + 0.2 - 2, 'NL-A-8.61', fontsize=10, color='w')
plt.text(5 - 0.3, 9.14 + 0.2 - 2, 'NL-A-9.14', fontsize=10, color='w')
plt.text(6 - 0.3, 9.24 + 0.2 - 2, 'NL-A-9.24', fontsize=10, color='w')


#NL TOP
plt.text(0 - 0.3, 8.80 + 0.2 - 2, 'NL-T-8.80', fontsize=10, color='w')
plt.text(1 - 0.3, 9.65 + 0.2 - 2, 'NL-T-9.65', fontsize=10, color='w')
plt.text(2 - 0.3, 11.60 + 0.2 - 2, 'NL-T-11.60', fontsize=10, color='w')
plt.text(3 - 0.3, 10.93 + 0.2 - 2, 'NL-T-10.93', fontsize=10, color='w')
plt.text(4 - 0.3, 9.85 + 0.2 - 2, 'NL-T-9.85', fontsize=10, color='w')
plt.text(5 - 0.3, 10.78 + 0.2 - 2, 'NL-T-10.78', fontsize=10, color='w')
plt.text(6 - 0.3, 11.13 + 0.2 - 2, 'NL-T-11.13', fontsize=10, color='w')

#BC
plt.text(0 - 0.3, 20.23 + 0.2 - 2, 'BC-20.23', fontsize=10, color='w')
plt.text(1 - 0.3, 28.35 + 0.2 - 2, 'BC-28.35', fontsize=10, color='w')
plt.text(2 - 0.3, 25.25 + 0.2 - 2, 'BC-25.25', fontsize=10, color='w')
plt.text(3 - 0.3, 27.63 + 0.2 - 2, 'BC-27.63', fontsize=10, color='w')
plt.text(4 - 0.3, 27.05 + 0.2 - 2, 'BC-27.05', fontsize=10, color='w')
plt.text(5 - 0.3, 25.13 + 0.2 - 2, 'BC-25.13', fontsize=10, color='w')
plt.text(6 - 0.3, 28.05 + 0.2 - 2, 'BC-28.05', fontsize=10, color='w')


#FDR
plt.text(0 - 0.3, 24.63 + 0.2 - 2, 'FDR-24.63', fontsize=10, color='w')
plt.text(1 - 0.3, 29.30 + 0.2 - 2, 'FDR-29.30', fontsize=10, color='w')
plt.text(2 - 0.3, 27.65 + 0.2 - 2, 'FDR-27.65', fontsize=10, color='w')
plt.text(3 - 0.3, 28.90 + 0.2 - 2, 'FDR-28.90', fontsize=10, color='w')
plt.text(4 - 0.3, 28.78 + 0.2 - 2, 'FDR-28.78', fontsize=10, color='w')
plt.text(5 - 0.3, 27.58 + 0.2 - 2, 'FDR-27.58', fontsize=10, color='w')
plt.text(6 - 0.3, 29.03 + 0.2 - 2, 'FDR-29.03', fontsize=10, color='w')


plt.show()



