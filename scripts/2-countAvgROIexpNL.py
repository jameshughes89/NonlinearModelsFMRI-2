'''
Counts the number of ROI in the average expression generated by the GP system

'''


from pylab import *
import csv
import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects):
    # attach some text labels
    for rect in rects:
		if rect.get_x() < 20.6 or rect.get_x() >= 21.6:
			height = rect.get_height()
			ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%(height), ha='center', va='bottom')


tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419]


fileLocation = '../outs/'
AverageROIAppearNL = []
AverageROITotal = []

lastsCount = 0
for t in tasks:
	allCounts = []
	avgCount = []

	for s in subjects:
		try:
			fCount = np.zeros(30)
			#print s
			for i in range(0,100):
				roiCount = 0
				inFile = csv.reader(open(fileLocation + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z/"+ str(i) + '_multi.txt','r'), delimiter='\t')

				fBool = [False] * 30			
				for line in inFile:
					if(line[-1][0] == 'v'):
						eInt = int(line[-1][1:])
				
						if(not(fBool[eInt])):
							roiCount += 1
							fBool[eInt] = True
							fCount[eInt] += 1
				avgCount.append(roiCount + 1)		# +1 because left hand side of 


			fCount[-1] = fCount[int(lasts[lastsCount])-1]
			fCount[int(lasts[lastsCount])-1] = 100
			print fCount
			allCounts.append(fCount)
		except IOError:
			continue			
			#print "OMGZ@!!1!, " + t + "_" + str(s) + " was not there!!!!"

	print t, np.mean(avgCount), np.std(avgCount)
	AverageROITotal.append(np.mean(avgCount))
	lastsCount += 1

	AverageROIAppearNL.append(np.mean(allCounts,axis=0))


AverageROIAppearSameDF = []
lastsCount = 0
for t in tasks:
	# 30 because that's the number of ROI
	count = np.zeros(30)
	for s in subjects:
		inputMatrix = list(csv.reader(open("/media/james/My Passport/HCP/HCP-Processed/" +t + "/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z.csv",'r')))
		inputMatrix = np.array(inputMatrix).astype(float).transpose()
		corMatrix = abs(np.corrcoef(inputMatrix))				#MAKE MATRIX

		# get the top correlated ROIs
		topX = np.argsort(corMatrix[-1,:])[-(int(AverageROITotal[lastsCount])+2):]
		print topX
		# for each of the ROIs in the top, add that to the count
		for top in topX:
			count[top]+=1

	# swap the last ROI and the ROI from the lasts
	# **remember, the 'last' roi is the one we forced on the left 
	count[-1] = count[int(lasts[lastsCount])-1]
	count[int(lasts[lastsCount])-1] = len(subjects)
	AverageROIAppearSameDF.append(count)
	lastsCount+=1


for i,t in enumerate(tasks):
	plt.bar(arange(1,31)-0.2, AverageROIAppearNL[i]/100,width=0.4)
	plt.bar(arange(1,31)+0.2, AverageROIAppearSameDF[i]/len(subjects),color='g',width=0.4)
	plt.title(t)
	plt.show()


		

