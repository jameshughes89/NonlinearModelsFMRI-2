'''

Does linear models traind on LR on LR data.

'''

import csv
import math
import numpy as np
import matplotlib.pyplot as plt

# BC
import bestExpressions_L_BC_EMOTION as emotion_BC	
import bestExpressions_L_BC_GAMBLING as gambling_BC	
import bestExpressions_L_BC_LANGUAGE as language_BC		
import bestExpressions_L_BC_MOTOR as motor_BC		
import bestExpressions_L_BC_RELATIONAL as relational_BC
import bestExpressions_L_BC_SOCIAL as social_BC
import bestExpressions_L_BC_WM as wm_BC

functions_BC = [emotion_BC.getFuncs(), gambling_BC.getFuncs(), language_BC.getFuncs(), motor_BC.getFuncs(), relational_BC.getFuncs(), social_BC.getFuncs(), wm_BC.getFuncs()]

import bestExpressions_L_BC_EMOTION_LASSO_1 as emotion_BC_LASSO
import bestExpressions_L_BC_GAMBLING_LASSO_1 as gambling_BC_LASSO	
import bestExpressions_L_BC_LANGUAGE_LASSO_1 as language_BC_LASSO
import bestExpressions_L_BC_MOTOR_LASSO_1 as motor_BC_LASSO
import bestExpressions_L_BC_RELATIONAL_LASSO_1 as relational_BC_LASSO
import bestExpressions_L_BC_SOCIAL_LASSO_1 as social_BC_LASSO
import bestExpressions_L_BC_WM_LASSO_1 as wm_BC_LASSO

functions_BC_LASSO = [emotion_BC_LASSO.getFuncs(), gambling_BC_LASSO.getFuncs(), language_BC_LASSO.getFuncs(), motor_BC_LASSO.getFuncs(), relational_BC_LASSO.getFuncs(), social_BC_LASSO.getFuncs(), wm_BC_LASSO.getFuncs()]

# FDR
import bestExpressions_L_FDR_EMOTION as emotion_FDR	
import bestExpressions_L_FDR_GAMBLING as gambling_FDR	
import bestExpressions_L_FDR_LANGUAGE as language_FDR		
import bestExpressions_L_FDR_MOTOR as motor_FDR		
import bestExpressions_L_FDR_RELATIONAL as relational_FDR
import bestExpressions_L_FDR_SOCIAL as social_FDR
import bestExpressions_L_FDR_WM as wm_FDR

functions_FDR = [emotion_FDR.getFuncs(), gambling_FDR.getFuncs(), language_FDR.getFuncs(), motor_FDR.getFuncs(), relational_FDR.getFuncs(), social_FDR.getFuncs(), wm_FDR.getFuncs()]

import bestExpressions_L_FDR_EMOTION_LASSO_1 as emotion_FDR_LASSO
import bestExpressions_L_FDR_GAMBLING_LASSO_1 as gambling_FDR_LASSO	
import bestExpressions_L_FDR_LANGUAGE_LASSO_1 as language_FDR_LASSO
import bestExpressions_L_FDR_MOTOR_LASSO_1 as motor_FDR_LASSO
import bestExpressions_L_FDR_RELATIONAL_LASSO_1 as relational_FDR_LASSO
import bestExpressions_L_FDR_SOCIAL_LASSO_1 as social_FDR_LASSO
import bestExpressions_L_FDR_WM_LASSO_1 as wm_FDR_LASSO

functions_FDR_LASSO = [emotion_FDR_LASSO.getFuncs(), gambling_FDR_LASSO.getFuncs(), language_FDR_LASSO.getFuncs(), motor_FDR_LASSO.getFuncs(), relational_FDR_LASSO.getFuncs(), social_FDR_LASSO.getFuncs(), wm_FDR_LASSO.getFuncs()]

# TOP 30
import bestExpressions_L_TOP30_EMOTION as emotion_TOP30	
import bestExpressions_L_TOP30_GAMBLING as gambling_TOP30	
import bestExpressions_L_TOP30_LANGUAGE as language_TOP30		
import bestExpressions_L_TOP30_MOTOR as motor_TOP30		
import bestExpressions_L_TOP30_RELATIONAL as relational_TOP30
import bestExpressions_L_TOP30_SOCIAL as social_TOP30
import bestExpressions_L_TOP30_WM as wm_TOP30

functions_TOP30 = [emotion_TOP30.getFuncs(), gambling_TOP30.getFuncs(), language_TOP30.getFuncs(), motor_TOP30.getFuncs(), relational_TOP30.getFuncs(), social_TOP30.getFuncs(), wm_TOP30.getFuncs()]

import bestExpressions_L_TOP30_EMOTION_LASSO_1 as emotion_TOP30_LASSO
import bestExpressions_L_TOP30_GAMBLING_LASSO_1 as gambling_TOP30_LASSO	
import bestExpressions_L_TOP30_LANGUAGE_LASSO_1 as language_TOP30_LASSO
import bestExpressions_L_TOP30_MOTOR_LASSO_1 as motor_TOP30_LASSO
import bestExpressions_L_TOP30_RELATIONAL_LASSO_1 as relational_TOP30_LASSO
import bestExpressions_L_TOP30_SOCIAL_LASSO_1 as social_TOP30_LASSO
import bestExpressions_L_TOP30_WM_LASSO_1 as wm_TOP30_LASSO

functions_TOP30_LASSO = [emotion_TOP30_LASSO.getFuncs(), gambling_TOP30_LASSO.getFuncs(), language_TOP30_LASSO.getFuncs(), motor_TOP30_LASSO.getFuncs(), relational_TOP30_LASSO.getFuncs(), social_TOP30_LASSO.getFuncs(), wm_TOP30_LASSO.getFuncs()]

# NL
import allExpressions_NL_EMOTION as emotion_NL
import allExpressions_NL_GAMBLING as gambling_NL
import allExpressions_NL_LANGUAGE as language_NL
import allExpressions_NL_MOTOR as motor_NL		
import allExpressions_NL_RELATIONAL as relational_NL
import allExpressions_NL_SOCIAL as social_NL
import allExpressions_NL_WM as wm_NL

functions_NL = [emotion_NL.getFuncs(), gambling_NL.getFuncs(), language_NL.getFuncs(), motor_NL.getFuncs(), relational_NL.getFuncs(), social_NL.getFuncs(), wm_NL.getFuncs()]


def calcFunctionError(f, data):
	allErrors = []
	for l in data:
		try:
			allErrors.append(abs(l[-1] - f(*l)))
		except Exception:
			allErrors.append(float('nan'))
		if allErrors[-1] > 100:
			del allErrors[-1]
	return np.nanmean(allErrors)


tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
#tasks = ["LANGUAGE"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#lasts = ["16"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816, 103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923, 106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123, 109325, 110411, 111312, 111413, 111514, 111716, 112819, 113215, 113619, 113821, 113922, 114419, 114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111, 120212, 120515, 121315, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422, 124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013, 130316, 130922, 131217, 131722, 131924, 132118, 133019, 133625, 133827, 133928, 134324, 135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231, 138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142424, 142626, 142828, 143325, 144226, 144832, 145531, 145834]

subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,
           103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,
           106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,
           109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419]


#subjects =[100307, 100408, 101006]


pltz = []

for taskCount, t in enumerate(tasks):

	# will keep track of the number of times each of the models was the best
	smallestCount = [0,0,0,0,0,0,0]
	smallestCountNOALL = [0,0,0,0,0,0]
	
	axes = plt.subplot2grid((1,7), (0, taskCount))
	pltz.append(axes)
	pltz[taskCount].set_title(t)

	for subjectCount, s in enumerate(subjects):
		#print t, s

		data = np.array(list(csv.reader(open("/home/james/Desktop/nData/" + t + "_"+str(s)+"_2_L" + lasts[taskCount] + '_Z.csv','r')))).astype(float)
		
		error_BC = calcFunctionError(functions_BC[taskCount][subjectCount], data)
		error_BC_LASSO = calcFunctionError(functions_BC_LASSO[taskCount][subjectCount], data)
		error_FDR = calcFunctionError(functions_FDR[taskCount][subjectCount], data)
		error_FDR_LASSO = calcFunctionError(functions_FDR_LASSO[taskCount][subjectCount], data)
		error_TOP30 = calcFunctionError(functions_TOP30[taskCount][subjectCount], data)
		error_TOP30_LASSO = calcFunctionError(functions_TOP30_LASSO[taskCount][subjectCount], data)

		error_NL = []

		# for each of the 100 models generated for each subject task combo
		for i in range(100):
			error_NL.append(calcFunctionError(functions_NL[taskCount][subjectCount][i], data))
		
		#np.nan_to_num(error_NL, copy=False)
		error_NL = [x for x in error_NL if not(math.isnan(x))]

		# NL, BCL, FDRL, CB, FDR, TOPL, TOP
		
		
		errorVector = [np.min(error_NL), error_BC_LASSO, error_FDR_LASSO, error_BC, error_FDR, error_TOP30_LASSO, error_TOP30]
		smallestCount[np.argmin(errorVector)]+=1

		errorVector = [np.min(error_NL), error_BC_LASSO, error_FDR_LASSO, error_BC, error_FDR, error_TOP30_LASSO]
		smallestCountNOALL[np.argmin(errorVector)]+=1

	print t
	print smallestCount 
	print smallestCountNOALL

		






























		

