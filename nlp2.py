import numpy as np
from sklearn.cluster import KMeans
import numpy as np
import os,io,math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA,KernelPCA,LatentDirichletAllocation,TruncatedSVD
from sklearn.metrics.cluster import contingency_matrix
from sklearn import metrics

scaler = StandardScaler(with_mean=True)

def write2d(file, header, arr, actuallabels, y):
	file.write(header+"\n")
	for i in arr:
		for j in i:
			file.write(str(j)+" ")
		file.write("\n")
	file.write("adjusted rank index: "+str(metrics.adjusted_rand_score(actuallabels,y))+"\n")
	file.write("completeness: "+str(metrics.completeness_score(actuallabels,y))+"\n")
	file.write("v-measure: "+str(metrics.v_measure_score(actuallabels,y))+"\n")
	file.write("homogeneity: "+str(metrics.homogeneity_score(actuallabels,y))+"\n")
	file.write("\n")

files=list()
cnt=0
dir=os.path.join(os.getcwd(),'combined')
for f in os.listdir(dir):
	if f.endswith(".txt"):
		cnt+=1
		files.append(os.path.join(dir,f))
file_iter = iter(files)

opt_file = io.open("output.txt", 'w')

vectorizer = TfidfVectorizer(analyzer='word',input='filename',token_pattern='[^\n\,\.\s\!\'\?\"\:\;\`\~\)\(\-0123456789][^\n\?\,\.\s\!\'\"\;\:\`\~\)\(\-0123456789]+')
X=vectorizer.fit_transform(file_iter,'ds141')        
X=X.toarray()
actuallabels=[0]*21 + [1]*9 + [2]*30 + [3]*49 + [4]*17
km = KMeans(n_clusters=3, init='k-means++',n_init=20)
print('data scaled and predicted dimnesions is :'+str(X.shape))
y=km.fit_predict(X)
print("tfidf"+str(X[0].shape))
confusion=contingency_matrix(actuallabels,y)
write2d(opt_file, "tfidf", confusion, actuallabels, y)
print("tfidf-done")


for i in range(cnt-60,cnt+1,10):
	pca = PCA(n_components=i)
	pc = pca.fit_transform(X)
	km = KMeans(n_clusters=3, init='k-means++',n_init=20)
	y=km.fit_predict(pc)
	print("PCA"+str(pca.n_components)+"-done")
	confusion = contingency_matrix(actuallabels,y)
	write2d(opt_file, "PCA"+str(pca.n_components), confusion, actuallabels, y)
	

for i in range(cnt-60,cnt,10):
	kpcal = KernelPCA(n_components=i,kernel='linear')
	kpcl = kpcal.fit_transform(X)
	km = KMeans(n_clusters=3, init='k-means++',n_init=20)
	y=km.fit_predict(kpcl)
	print("KPCAlin"+str(kpcal.n_components)+"-done")
	confusion=contingency_matrix(actuallabels,y)
	write2d(opt_file, "KPCAlin"+str(kpcal.n_components), confusion, actuallabels, y)

for i in range(cnt-60,cnt,10):
	kpcap = KernelPCA(n_components=i,kernel='poly')
	kpcp = kpcap.fit_transform(X)
	km = KMeans(n_clusters=3, init='k-means++',n_init=20)
	y=km.fit_predict(kpcp)
	print("kpcapoly"+str(kpcap.n_components)+"-done")
	confusion=contingency_matrix(actuallabels,y)
	write2d(opt_file, "kpcapoly"+str(kpcap.n_components), confusion, actuallabels, y)

for i in range(cnt-60,cnt,10):
	kpcac = KernelPCA(n_components=i,kernel='cosine')
	kpcc = kpcac.fit_transform(X)
	km = KMeans(n_clusters=3, init='k-means++',n_init=20)
	y=km.fit_predict(kpcc)
	print("kpcacos"+str(kpcac.n_components)+"-done")
	confusion=contingency_matrix(actuallabels,y)
	write2d(opt_file, "kpcacos"+str(kpcac.n_components), confusion, actuallabels, y)

for i in range(cnt-60,cnt,10):
	kpcas = KernelPCA(n_components=i,kernel='sigmoid')
	kpcs = kpcas.fit_transform(X)
	km = KMeans(n_clusters=3, init='k-means++',n_init=20)
	y=km.fit_predict(kpcs)
	print("kpcasig"+str(kpcas.n_components)+"-done")
	confusion=contingency_matrix(actuallabels,y)
	write2d(opt_file, "kpca-sig"+str(kpcas.n_components), confusion, actuallabels, y)

for i in range(cnt-60,cnt+1,10):
	lda = LatentDirichletAllocation(n_components=i,learning_method='batch')
	ldc = lda.fit_transform(X)
	km = KMeans(n_clusters=3, init='k-means++',n_init=20)
	y=km.fit_predict(ldc)
	print("LDA"+str(lda.n_components)+"-done")
	confusion=contingency_matrix(actuallabels,y)
	write2d(opt_file, "LDA"+str(lda.n_components), confusion, actuallabels, y)


for i in range(cnt-60,cnt+1,10):
	tsvd = TruncatedSVD(n_components=i)
	tsvc = tsvd.fit_transform(X)
	km = KMeans(n_clusters=3, init='k-means++',n_init=20)
	y=km.fit_predict(tsvc)
	print("TSVD"+str(tsvd.n_components))
	confusion=contingency_matrix(actuallabels,y)
	write2d(opt_file, "TSVD"+str(tsvd.n_components), confusion, actuallabels, y)