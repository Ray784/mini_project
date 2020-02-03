import numpy as np
import os,io,math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA,KernelPCA,TruncatedSVD
from sklearn.metrics.cluster import contingency_matrix
from sklearn import metrics
import time
import pandas as pd
from pandas.plotting import scatter_matrix


def write2d(file, header, arr, actuallabels, y, db):
	file.write(header+"\n")
	for i in arr:
		for j in i:
			file.write(str(j)+" ")
		file.write("\n")
	file.write("accuracy rate: "+str(findAccuracy(arr))+"\n")
	file.write("adjusted rank index: "+str(metrics.adjusted_rand_score(actuallabels,y))+"\n")
	file.write("completeness: "+str(metrics.completeness_score(actuallabels,y))+"\n")
	file.write("v-measure: "+str(metrics.v_measure_score(actuallabels,y))+"\n")
	file.write("homogeneity: "+str(metrics.homogeneity_score(actuallabels,y))+"\n")
	file.write("davies_bouldin_score: "+str(db)+"\n")
	file.write("\n")

	table.write(str(round(metrics.adjusted_rand_score(actuallabels,y), 4))+", "+str(round(metrics.completeness_score(actuallabels,y), 4))+", "
		+str(round(metrics.v_measure_score(actuallabels,y), 4))+", "+str(round(metrics.homogeneity_score(actuallabels,y), 4))+"\n")


def findAccuracy(confusion):
	acc1 = [confusion[0], confusion[2], confusion[1]]
	acc2 = [confusion[1], confusion[0], confusion[2]]
	acc = max(diag(acc1), diag(acc2), diag(confusion))
	return (acc/141)*100

def diag(matrix):
	diag1 = 0
	diag2 = 0
	for i in range(len(matrix)):
		diag1 += matrix[i][i]
	for i in range(len(matrix)):
		diag2 += matrix[i][len(matrix)-1-i]
	return max(diag1, diag2)


def doClusters(num_clusters, reducer, X, opt_file, i):
	start = time.time()
	if(reducer == 'pca'):
		pca = PCA(n_components=i)
		X = pca.fit_transform(X)
		if(i == 141):
			for j in range(i):
				file = io.open(folder_name+"-out"+"\\pca\\pca-"+str(j)+".txt", 'w', encoding="utf-8")
				file.write("num_words "+str(len(words))+"\n\n")
				for val in range(len(pca.components_[j])):
					file.write(words[val]+	" :"+str(pca.components_[j][val]) + "\n")
			#print(pca.explained_variance_)
	elif(reducer == 'kpca,lin'):
		kpcal = KernelPCA(n_components=i,kernel='linear')
		X = kpcal.fit_transform(X)
	elif(reducer == 'kpca,poly'):
		kpcap = KernelPCA(n_components=i,kernel='poly')
		X = kpcap.fit_transform(X)
	elif(reducer == 'kpca,cos'):
		kpcac = KernelPCA(n_components=i,kernel='cosine')
		X = kpcac.fit_transform(X)
	elif(reducer == 'kpca,sig'):
		kpcas = KernelPCA(n_components=i,kernel='sigmoid')
		X = kpcas.fit_transform(X)
	elif(reducer == 'none' and i != 141):
		return;
	rt = time.time()-start
	start = time.time()
	km = KMeans(n_clusters=num_clusters, init='k-means++', n_init=20, random_state= 0)
	y=km.fit_predict(X)
	ct = time.time()-start

	if(reducer == 'none'): 
		reducer = 'tfidf'
		i = 18872

	time_file.write("\n"+reducer+"--"+str(i)+"\n"+str(rt)+"\n"+str(ct)+"\n"+str(rt+ct)+"\n")
	print("reducer: "+reducer+": "+str(i)+" dims - done")
	confusion=contingency_matrix(actuallabels,y)
	
	dr = (i/141)*100
	db = round(metrics.davies_bouldin_score(X,y),4)
	table.write(str(i)+", "+str(round(100-dr,4))+", "+str(db)+", ")
	write2d(opt_file, reducer+"--"+str(i), confusion, actuallabels, y, db)




folder_name = 'ds-141-3'
num_clusters = 3
opt_file = io.open(folder_name+"-out"+"\\output.txt", 'w')
time_file = io.open(folder_name+"-out"+"\\time_opt.txt", "w")
table = io.open(folder_name+"-out"+"\\table.txt", "w")
#cluster_file = io.open("clusters.txt", "w")
reducers = ['none', 'pca', 'kpca,lin', 'kpca,poly', 'kpca,cos', 'kpca,sig']
actuallabels=[0]*47 + [1]*47 + [2]*47
time_file.write("reducer--num_comps\nreduce time\ncluster time\ntotal time\n")




files=list()
cnt=0
dir=os.path.join(os.getcwd(),folder_name)
for f in os.listdir(dir):
	if f.endswith(".txt"):
		cnt+=1
		files.append(os.path.join(dir,f))
file_iter = iter(files)
 
vectorizer = TfidfVectorizer(analyzer='word',input='filename', 
	token_pattern='[^\n\,\.\s\!\'\?\"\:\;\`\~\)\(\-0123456789][^\n\?\,\.\s\!\'\"\;\:\`\~\)\(\-0123456789]+')
X=vectorizer.fit_transform(file_iter,folder_name)  
words = vectorizer.get_feature_names()
X=X.toarray()

for reducer in reducers:
	table.write("\n"+reducer+"\n");
	table.write("num_comps,dr%,DBI,ARI,completeness,v_measure,homogeneity\n")
	for i in range(cnt,cnt-59,-5):
		try:
			x = X
			doClusters(num_clusters, reducer, x, opt_file, i)
		except Exception as e:
			print(e)
	table.write("\n");

