'''
Takes the expressions and generate their absolute error (as opposed to MSE)
'''

import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr  


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
#lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123]


outData = []
#lastsCount = 0
for lastsCount,t in enumerate(tasks):

	# load up the best expressions for the respective task
	bexp = __import__('bestExpressions-NL=' + t)
	funcsNL = bexp.getFuncs()
	

	#allError = 0
	#allErrorList = []
	#count = 0
	
	oFile = open('./topModels/bestExpressionsError-NL-' + t + '.txt','w')
	for index, s in enumerate(subjects):
		try:
			data = np.array(list(csv.reader(open("/media/james/My Passport/HCP/HCP-Processed/" +t + "/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z.csv",'r')))).astype(float)


			singleError = 0
			numLines = 0
			
			# for plotting I think
			#Xs = range(len(data))

			#YsNL = []
			#YsL = []
			yNLabs = 0
			#yLabs = 0
			#diffabs = 0

			#yNLmse = 0
			#yLmse = 0
			#diffmse = 0


			#for i in range(len(v29)):
			for modelCount, l in enumerate(data)
				#use count, it works when skppling subjects. 
				try:
					#yNL = funcsNL[count](v0[i],v1[i],v2[i],v3[i],v4[i],v5[i],v6[i],v7[i],v8[i],v9[i],v10[i],v11[i],v12[i],v13[i],v14[i],v15[i],v16[i],v17[i],v18[i],v19[i],v20[i],v21[i],v22[i],v23[i],v24[i],v25[i],v26[i],v27[i],v28[i],v29[i])
					yNL = funcsNL[modelCount](*l)
				except OverflowError:
					print "\tOverrrrflow!"
					# if some weird overflow issue, take the average of all poitns so far. 
					yNL = np.mean(yNLabs)

				yNLabs = yNLabs + abs(yNL - l[-1])			


			yNLabs = yNLabs/len(data)


			#print s, yNLabs, yLabs, diffabs, yNLmse, yLmse, diffmse
			#outData.append([yNLabs])

			print t, s, yNLabs			
			
			oFile.write(str(yNLabs) + '\n')			
			'''	
			print yabs/len(v29)
			print yLabs/len(v29)
			print diffabs/len(v29)
			print "------"
			print ymse/len(v29)
			print yLmse/len(v29)
			print diffmse/len(v29)
		

			#plt.plot(Xs, v29 'go')
			plt.plot(Xs, v29 'b', label='measured')
			plt.plot(Xs, Ys, 'r', label='SR-butLin')
			plt.plot(Xs, YsL, 'g', label='GLM-Top 3')
			plt.legend()
			plt.show()
			'''

		'''
			count += 1		#ONLY INCREASE COUNT WHEN WE SUCESSFULLY DID EVAL
		except IOError:	
			print "OMGZ@!!1!, " + t + "_" + str(s) + " was not there!!!!"			
			continue
		'''
		
	#lastsCount += 1
	oFile.close()



