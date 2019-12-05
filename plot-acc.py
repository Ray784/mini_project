import numpy as np
import matplotlib.pyplot as plt

labels = ['tfidf','pca-141','kpca-lin-141','kpca-poly-141','kpca-cos-141','kpca-sig-141']
performance = [1.838083028793335, 0.0388941764831543, 0.037934303283691406, 0.038895606994628906, 0.039893388748168945, 0.03789830207824707]
index = np.arange(len(labels))


plt.bar(index, performance)
plt.xlabel('Dimensionality Reduction')
plt.ylabel('Time')
plt.title('Clustering Time')
plt.xticks(index, labels, rotation=30)
plt.show()