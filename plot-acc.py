import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('tfidf','pca-141','kpca-lin-141','kpca-poly-141','kpca-cos-141','kpca-sig-141')
y_pos = np.arange(len(objects))
performance = [27.816042613802655, 23.038716169015527, 32.0788003528374, 35.89344033450853, 33.747229251260324]

plt.bar([1,2,3,4,5,6], performance, align='center')
plt.xlabel('percentage accuracy')
plt.title('adjusted rank index')

plt.show()