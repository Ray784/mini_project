if(reducer == 'pca' and i==141):
		
		data = pd.DataFrame(X[:,:10], columns=['x1', 'x2', 'x3',
                    'x4','x5','x6','x7','x8','x9','x10'])
		k = scatter_matrix(data, alpha=0.2, figsize=(6, 6), diagonal='hist')
		plt.show()