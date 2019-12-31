def findAccuracy(confusion):
	acc1 = [confusion[0], confusion[2], confusion[1]]
	acc2 = [confusion[1], confusion[0], confusion[2]]
	acc = max(diag(acc1), diag(acc2), diag(confusion))
	return acc

def diag(matrix):
	diag1 = 0
	diag2 = 0
	for i in range(len(matrix)):
		diag1 += matrix[i][i]
	for i in range(len(matrix)):
		diag2 += matrix[i][len(matrix)-1-i]
	return max(diag1, diag2)


confusion = [[15, 1, 31], [31, 2, 14], [11, 33, 3]]
print(findAccuracy(confusion))