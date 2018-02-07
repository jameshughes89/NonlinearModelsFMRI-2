'''

creates a large distance matrix for all non liear models. 

Does linear models traind on LR on LR data.

'''

import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


import bestExpressions_L_TOP30_EMOTION as emotion		
import bestExpressions_L_TOP30_GAMBLING as gambling	
import bestExpressions_L_TOP30_LANGUAGE as language		
import bestExpressions_L_TOP30_MOTOR as motor		
import bestExpressions_L_TOP30_RELATIONAL as relational		
import bestExpressions_L_TOP30_SOCIAL as social
import bestExpressions_L_TOP30_WM as wm

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816, 103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923, 106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123, 109325, 110411, 111312, 111413, 111514, 111716, 112819, 113215, 113619, 113821, 113922, 114419, 114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111, 120212, 120515, 121315, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422, 124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013, 130316, 130922, 131217, 131722, 131924, 132118, 133019, 133625, 133827, 133928, 134324, 135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231, 138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142424, 142626, 142828, 143325, 144226, 144832, 145531, 145834]

subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,
           103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,
           106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,
           109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419]

#all_functions_line = funcsL_EMOTION[:len(subjects)] + funcsL_GAMBLING[:len(subjects)] + funcsL_LANGUAGE[:len(subjects)] + funcsL_MOTOR[:len(subjects)] + funcsL_RELATIONAL[:len(subjects)] + funcsL_SOCIAL[:len(subjects)] + funcsL_WM[:len(subjects)]

all_functions_line = emotion.getFuncs() + gambling.getFuncs() + language.getFuncs() + motor.getFuncs() + relational.getFuncs() + social.getFuncs() + wm.getFuncs()

matrixMSE = []
matrixABE = []

matrixMIN = []


lastsCount = 0

for t in tasks:
	fs='funcsL_' + t + ' = ['
	count = 0
	for s in subjects:
		print t, s
		ALL = []

		iFile = csv.reader(open("/home/james/Desktop/nData/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z.csv",'r'))
		for l in iFile:
			ALL.append(l)

		ALL = np.array(ALL)
		ALL = ALL.astype(float)
		allmsE = []
		allabE = []
		

		for f in all_functions_line:

			try:			
				msE = []
				abE = []			
				for l in ALL:
					try:
						err = l[-1] - f(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17],l[18],l[19],l[20],l[21],l[22],l[23],l[24],l[25],l[26],l[27],l[28],l[29])
						msE.append(err**2)
						abE.append(abs(err))
					except(ValueError, OverflowError, ZeroDivisionError): 
						msE.append(float('nan'))
						abE.append(float('nan'))
				
				allmsE.append((np.mean(msE)))
				allabE.append((np.mean(abE)))
				#allmsE.append(log(np.mean(msE)))
				#allabE.append(log(np.mean(abE)))
			except Exception:
				print '\t\t\tBBBBBUSTTTEDDDD: ', t, s
				allmsE.append(np.float('nan'))
				allabE.append(np.float('nan'))
				continue


		matrixMSE.append(allmsE)
		matrixABE.append(allabE)

		allmin = np.zeros(len(allabE))
		allmin[np.argsort(allabE)[0]] = 1
		matrixMIN.append(allmin)

	lastsCount +=1

np.savetxt('msEmat_L_LR-TOP30.csv', matrixMSE, delimiter=",")
np.savetxt('abEmat_L_LR-TOP30.csv', matrixABE, delimiter=",")
np.savetxt('minmat_L_LR-TOP30.csv', matrixMIN, delimiter=",")


		








