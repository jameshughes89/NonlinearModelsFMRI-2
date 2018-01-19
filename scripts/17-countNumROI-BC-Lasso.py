
import numpy as np
import csv
import sys
import thresh_methods as tm

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,
           103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,
           106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,
           109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419]

#tasks = ["MOTOR"]
#lasts = ["21"]
#subjects =[100307]

allBestVal = []
allBestInd = []
allmsE = []
allabE = []

allVarCounts = []

fileLocation = '../outs/'

lastsCount = 0
for t in tasks:
	count = 0
	sumCounts = []


	for s in subjects:
		#try:		
			X = []
			y = []
			ALL = []

			fCount = np.zeros(30)

			iFile = csv.reader(open("/home/james/Desktop/nData/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z.csv",'r'), delimiter=',')
			for l in iFile:
				X.append(l[:-1])
				y.append(l[-1])
				ALL.append(l)



			ALL = np.array(ALL)
			ALL = ALL.astype(float)

			X = np.array(X)
			y = np.array(y)
			X = X.astype(float)
			y = y.astype(float)

			nTRs = len(y)

			corrC = np.corrcoef(ALL.T)
			corrC = np.abs(corrC)					# DO ABS here because negative correlatoion is fine!
			thr = tm.bc_alpha(corrC, alpha=0.05)
			#corrC[corrC < thr] = 0
			signif = []
			for i, e in enumerate(corrC[-1]):
				if tm.RtoP(e, nTRs) < thr:
					signif.append(i)
			signif = signif[:-1]
			X = X.T[signif]	
			X = X.T

			# CHANGE THIS TO SK LEARN!
			#OLS STUFF
			#X = sm.add_constant(X)
			#rez = sm.OLS(y, X).fit()
			#B = rez.params
		
			import sklearn.linear_model
			reg = sklearn.linear_model.Lasso(alpha=0.1)
			reg.fit(X, y)

			B = []
			B = B + list(reg.coef_)


			for i in range(len(B)):
				if B[i] > 0:
					if i == (int(lasts[lastsCount]) - 1):
						fCount[29] += 1
					elif i == 29:
						fCount[int(lasts[lastsCount]) - 1] += 1
					else:
						fCount[i] += 1


			sumCounts.append(fCount)
	allVarCounts.append(np.sum(sumCounts,axis=0))

	lastsCount+=1

np.savetxt('roiCount_BC_Lasso.csv', allVarCounts, delimiter=",")




