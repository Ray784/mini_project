import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#cellNames1 = ['Number of components Chosen using - ', 'DR acheived in %', 'Davies Bouldin Index']
def plotTable(reducer, data1, data2):
	cellNames1 = ['Number of\ncomponents\nchosen using ', 'DR %', 'Davies Bouldin\nIndex']
	cellNames2 = ['Adjusted\n Rand Index', 'Completeness', 'V-measure', 'Homogeneity']
	cellNames1[0]+=reducer

	plt.subplots_adjust(left=0.25, top=0.8, right=0.75)
	plt.axis('off')
	table1 = plt.table(cellText=data1,colLabels=cellNames1, colWidths=[0.3] * 3, loc='center')
	table1.set_fontsize(30)
	table1.scale(2, 2)
	plt.show()

	plt.subplots_adjust(left=0.26, top=0.8, right=0.74)
	plt.axis('off')
	table2 = plt.table(cellText=data2,colLabels=cellNames2, colWidths=[0.25] * 4, loc='center')
	table2.set_fontsize(30)
	table2.scale(2, 2)
	plt.show()

plotTable('PCA', [ [ 141, 0.0, 6.9209 ],
 [ 136, 3.5461, 6.9436 ],
 [ 131, 7.0922, 6.7552 ],
 [ 126, 10.6383, 6.7293 ],
 [ 121, 14.1844, 6.2741 ],
 [ 116, 17.7305, 6.6081 ],
 [ 111, 21.2766, 6.1794 ],
 [ 106, 24.8227, 5.6781 ],
 [ 101, 28.3688, 6.4085 ],
 [ 96, 31.9149, 4.1273 ],
 [ 91, 35.461, 6.3289 ],
 [ 86, 39.0071, 3.9251 ]] ,[ [ 0.2304, 0.2951, 0.289, 0.2831 ], 
[ 0.3702, 0.3618, 0.3609, 0.3599 ], 
[ 0.3481, 0.3991, 0.3958, 0.3926 ], 
[ 0.271, 0.3346, 0.3291, 0.3238 ], 
[ 0.16, 0.3294, 0.3024, 0.2795 ], 
[ 0.1788, 0.2342, 0.2293, 0.2246 ], 
[ 0.0372, 0.1001, 0.0846, 0.0732 ], 
[ 0.1189, 0.2406, 0.2093, 0.1851 ], 
[ 0.0867, 0.1718, 0.159, 0.148 ], 
[ 0.0366, 0.259, 0.1803, 0.1383 ], 
[ 0.2254, 0.2571, 0.2399, 0.2249 ], 
[ 0.0571, 0.2432, 0.1589, 0.118 ]])
