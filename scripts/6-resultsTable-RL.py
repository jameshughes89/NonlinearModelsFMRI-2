#generates a model with OLS in a weird way

import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import statsmodels.api as sm
import thresh_methods as tm



tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,
           103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,
           106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,
           109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419]



# losd the data
NLerrors = []
BCerrors = []
FDRerrors = []
BCLerrors = []
FDRLerrors = []
ALLerrors = []
ALLLerrors = []

for t in tasks:
	NLerrors.append(np.array(list(csv.reader(open('./topModels/bestExpressionsError-NL-' + t + '.txt','r')))).astype(float))
	BCLerrors.append(np.array(list(csv.reader(open('./topModels/bestExpressionsError-L-BC-' + t + '_LASSO_1.txt','r')))).astype(float))
	FDRLerrors.append(np.array(list(csv.reader(open('./topModels/bestExpressionsError-L-FDR-' + t + '_LASSO_1.txt','r')))).astype(float))
	BCerrors.append(np.array(list(csv.reader(open('./topModels/bestExpressionsError-L-BC-' + t + '.txt','r')))).astype(float))
	FDRerrors.append(np.array(list(csv.reader(open('./topModels/bestExpressionsError-L-FDR-' + t + '.txt','r')))).astype(float))
	ALLLerrors.append(np.array(list(csv.reader(open('./topModels/bestExpressionsError-L-TOP30-' + t + '_LASSO_1.txt','r')))).astype(float))
	ALLerrors.append(np.array(list(csv.reader(open('./topModels/bestExpressionsError-L-TOP30-' + t + '.txt','r')))).astype(float))



# formatted MEDIAN table for latex

for i, t in enumerate(tasks):
	print( t + '\t& ' + 
            str(round(np.median(NLerrors[i]),2)) + '\t& $\pm$' + str(round(scipy.stats.iqr(NLerrors[i])/2,2)) + '\t& ' + 
            str(round(np.median(BCLerrors[i]),2)) + '\t& $\pm$' + str(round(scipy.stats.iqr(BCLerrors[i])/2,2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], BCLerrors[i])[1]) + '\t& ' + 
            str(round(np.median(FDRLerrors[i]),2)) + '\t& $\pm$' + str(round(scipy.stats.iqr(FDRLerrors[i])/2,2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], FDRLerrors[i])[1]) + '\t& ' + 
            str(round(np.median(BCerrors[i]),2)) + '\t& $\pm$' + str(round(scipy.stats.iqr(BCerrors[i])/2,2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], BCerrors[i])[1]) + '\t& ' +
            str(round(np.median(FDRerrors[i]),2)) + '\t& $\pm$' + str(round(scipy.stats.iqr(FDRerrors[i])/2,2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], FDRerrors[i])[1]) + '\t& ' + 
            str(round(np.median(ALLLerrors[i]),2)) + '\t& $\pm$' + str(round(scipy.stats.iqr(ALLLerrors[i])/2,2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], ALLLerrors[i])[1]) + '\t& ' +
            str(round(np.median(ALLerrors[i]),2)) + '\t& $\pm$' + str(round(scipy.stats.iqr(ALLerrors[i])/2,2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], ALLerrors[i])[1]) + '\\\\' )


# formatted MEAN table for latex
print
print
print

for i, t in enumerate(tasks):
	print( t + '\t& ' + 
            str(round(np.mean(NLerrors[i]),2)) + '\t& ' + str(round(np.std(NLerrors[i]),2)) + '\t& ' + 
            str(round(np.mean(BCLerrors[i]),2)) + '\t& ' + str(round(np.std(BCLerrors[i]),2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], BCLerrors[i])[1]) + '\t& ' + 
            str(round(np.mean(FDRLerrors[i]),2)) + '\t& ' + str(round(np.std(FDRLerrors[i]),2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], FDRLerrors[i])[1]) + '\t& ' + 
            str(round(np.mean(BCerrors[i]),2)) + '\t& ' + str(round(np.std(BCerrors[i]),2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], BCerrors[i])[1]) + '\t& ' +
            str(round(np.mean(FDRerrors[i]),2)) + '\t& ' + str(round(np.std(FDRerrors[i]),2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], FDRerrors[i])[1]) + '\t& ' + 
            str(round(np.mean(ALLLerrors[i]),2)) + '\t& ' + str(round(np.std(ALLLerrors[i]),2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], ALLLerrors[i])[1]) + '\t& ' +
            str(round(np.mean(ALLerrors[i]),2)) + '\t& ' + str(round(np.std(ALLerrors[i]),2)) + '\t& ' + '{:0.2e}'.format(scipy.stats.mannwhitneyu(NLerrors[i], ALLerrors[i])[1]) + '\\\\ ' )











