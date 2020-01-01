import io
import numpy as np
import matplotlib.pyplot as plt

folder = "outputs-ds-t3-141"
time_file = io.open(folder+"\\time_opt.txt", "r")
string_of_all = time_file.read()

list_of_reducers = string_of_all.split("\n\n")
list_of_times = []

for string in list_of_reducers:
	list_of_times.append(string.split("\n"))

labels = []
reduce_times = []
cluster_times = []
total_times = []
allowed = ['141', '18872', '86', '116']

for i in range(1,len(list_of_times)):
	if list_of_times[i][0].split('--')[1] in allowed :
		labels.append(list_of_times[i][0])
		reduce_times.append(round(float(list_of_times[i][1]), 4))
		cluster_times.append(round(float(list_of_times[i][2]), 4))
		total_times.append(round(float(list_of_times[i][3]), 4))
index = np.arange(len(labels))

plt.subplots_adjust(left=0.15, top=0.85, bottom=0.35, right=0.85)
plt.bar(index, reduce_times)
plt.xlabel('Dimensionality Reduction')
plt.ylabel('Time')
plt.title('Dimensionality Reduction Time')
plt.xticks(index, labels, rotation=90)
plt.savefig('graphs\\dr_time.png')
plt.show()

plt.subplots_adjust(left=0.15, top=0.85, bottom=0.35, right=0.85)
plt.bar(index, cluster_times)
plt.xlabel('Dimensionality Reduction')
plt.ylabel('Time')
plt.title('Clustering Time')
plt.xticks(index, labels, rotation=90)
plt.savefig('graphs\\clustering_time.png')
plt.show()

plt.subplots_adjust(left=0.15, top=0.85, bottom=0.35, right=0.85)
plt.bar(index, total_times)
plt.xlabel('Dimensionality Reduction')
plt.ylabel('Time')
plt.title('Total Time')
plt.xticks(index, labels, rotation=90)
plt.savefig('graphs\\total_time.png')
plt.show()



