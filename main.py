import numpy as np
from sympy import *

input_matrix = np.array([
		[0.99, 0.41, 0.77, 0.92, 0.64],
		[0.2,  0.89, 0.7,  0.25, 0.38],
		[0.71, 0.55, 0.27, 0.38, 0.34],
		[0.04, 0.3,  0.5,  0.05, 0.45],
		[0.69, 0.32, 0.89, 0.42, 0.97]
])

input_matrix_transpose = np.array([
	[0.12, 0.3,  0.54, 0.75, 0.47],
	[0.4,  0.97, 0.89, 0.22, 0.71],
	[0.45, 0.92, 0.51, 0.12, 0.95],
	[0.2,  0.93, 0.31, 0.15, 0.05],
	[0.82, 0.41, 0.03, 0.6,  0.35]
])


def diagonal(input_matrix=input_matrix):
	"""
	Creates a new matrix  that is diagonal of the 'input_matrix' and
	a new list that contains values except 0 of the new matrix
	"""
	try:
		matrix_type = np.zeros((len(input_matrix), len(input_matrix[0])))
		list_type = []

		count = 0
		for lis in input_matrix:
			list_type.append(lis[count])
			matrix_type[count][count] = lis[count]
			count+=1

		return list_type, matrix_type
	except Exception as exception:
		print(exception)
		return "Input matrix is not square matrix"

def upper(input_matrix=input_matrix):
	"""Creates a new matrix that is upside of the diagonal of 'input_matrix'"""
	try:
		for i in range(len(input_matrix)):
			input_matrix[i][0:i] = 0
		return input_matrix
	except Exception as exception:
		print(exception)
		return "Input matrix is not square matrix"

def lower(input_matrix=input_matrix):
	"""Creates a new matrix that is downside of the diagonal of 'input_matrix'"""
	try:
		for i in range(len(input_matrix)-1):
			input_matrix[i][i+1:] = 0
		return input_matrix
	except Exception as exception:
		print(exception)
		return "Input matrix is not square matrix"

def banded(input_matrix=input_matrix, bandwidth=3):

	try:
		zeros_matrix = np.zeros((len(input_matrix), len(input_matrix)))	
		count = 0
		liste=[]
		for lis in input_matrix:
			if count == 0 or count == len(input_matrix) - 1:
				if count == 0:
					zeros_matrix[0][0:2] = input_matrix[0][0:2]
				else:
					zeros_matrix[-1][-1:-3] = input_matrix[-1][-1:-3]
			elif len(input_matrix) / count < len(input_matrix) / 2:
				liste.append(input_matrix[count][(count-1):(count+bandwidth-1)])
				zeros_matrix[count][(count-1):(count+bandwidth-1)] = input_matrix[count][(count-1):(count+bandwidth-1)]
			else:
				liste.append(input_matrix[count][(count-1):(count+bandwidth-1)])
				zeros_matrix[count][(count-1):(count+bandwidth-1)] = input_matrix[count][(count-1):(count+bandwidth-1)]
			
			count+=1
		return zeros_matrix
	except Exception as exception:
		print(exception)
		return "Input matrix is not square matrix"

def transpose(input_matrix=input_matrix_transpose):
	"""Creates a new matrix that is transpose of the 'input_matrix'"""
	try:
		new_matrix = np.zeros((len(input_matrix), len(input_matrix)))
		for i in range(len(input_matrix)):
			for j in range(len(input_matrix)):
				new_matrix[i][j] = input_matrix[j][i]
		return new_matrix
	except Exception as exception:
		print(exception)
		return "Input matrix is not square matrix"
