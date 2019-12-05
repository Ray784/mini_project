import numpy as np
import matplotlib.pyplot as plt

labels = ['tfidf','pca-141','kpca-lin-141','kpca-poly-141','kpca-cos-141','kpca-sig-141']
performance = [1.838083028793335, 0.8647186756134033, 0.07683062553405762, 0.0777587890625, 0.10372233390808105, 0.07878923416137695]
index = np.arange(len(labels))


plt.bar(index, performance)
plt.xlabel('Dimensionality Reduction')
plt.ylabel('Time')
plt.title('Total Time')
plt.xticks(index, labels, rotation=30)
plt.show()