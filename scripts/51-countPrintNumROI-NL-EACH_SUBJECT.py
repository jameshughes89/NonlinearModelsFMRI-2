
import numpy as np
import csv
import sys
import matplotlib.pylab as plt

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


fig = plt.figure(0)
pltz = []
fileLocation = '../outs/'

lastsCount = 0
for t in tasks:
	count = 0
	taskCountsPerSub = []

	axes = plt.subplot2grid((1,7), (0, lastsCount))
	pltz.append(axes)
	pltz[lastsCount].set_title(t, fontsize=12)
	if lastsCount == 0:
		pltz[lastsCount].set_ylabel('Subject')
	if lastsCount == 3:
		pltz[lastsCount].set_xlabel('Region of Interest')

	for s in subjects:	
		fcount = np.zeros(30)
		for i in range(100):
			iFile = csv.reader(open(fileLocation +  t + "_"+str(s)+"_2_L" + str(lasts[lastsCount]) + "_Z/"+ str(i) + '_multi.txt','r'), delimiter='\t')				#CHANGE HERE
			madeChange = [False]*30

			for line in iFile:
				if(line[-1][0] == 'v'):
					eInt = int(line[-1][1:])
					if not madeChange[eInt]:
						fcount[eInt] += 1
						madeChange[eInt] = True
	
		fcount[-1] = fcount[int(lasts[lastsCount]) - 1]
		fcount[int(lasts[lastsCount]) - 1] = 100			
		taskCountsPerSub.append(fcount)

	cmap = plt.get_cmap(lut=100)
	im = pltz[lastsCount].matshow(taskCountsPerSub, cmap=cmap, vmin=0, vmax=100)
	if lastsCount == 6:
		plt.colorbar(im, label='Count')
	pltz[lastsCount].set_xticks(range(5, 30,5))
	pltz[lastsCount].set_xticklabels(['5','10','15','20','25','30'], fontsize=10)
	#pltz[lastsCount].set_xticklabels(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"], fontsize=10)
	pltz[lastsCount].set_yticklabels([])	
	'''
	for asd, cas in enumerate(taskCountsPerSub):
		for sdf, c in enumerate(cas):
				plt.text(sdf-.4, asd+.2, int(c), fontsize=8)
	#plt.show()
	'''

	lastsCount+=1

#plt.suptitle('ROI Counts From All Models from All Subjects on All Tasks')
plt.show()

