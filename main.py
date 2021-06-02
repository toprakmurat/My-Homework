import numpy as np
from sympy import *

sample_input_matrix = np.array([
		[0.99, 0.41, 0.77, 0.92, 0.64],
		[0.2,  0.89, 0.7,  0.25, 0.38],
		[0.71, 0.55, 0.27, 0.38, 0.34],
		[0.04, 0.3,  0.5,  0.05, 0.45],
		[0.69, 0.32, 0.89, 0.42, 0.97]
])

sample_input_matrix_transpose = np.array([
	[0.12, 0.3,  0.54, 0.75, 0.47],
	[0.4,  0.97, 0.89, 0.22, 0.71],
	[0.45, 0.92, 0.51, 0.12, 0.95],
	[0.2,  0.93, 0.31, 0.15, 0.05],
	[0.82, 0.41, 0.03, 0.6,  0.35]
])

def is_squared(matrix):
    '''Check that all rows have the correct length, not just the first one'''
    return all(len(row) == len(matrix) for row in matrix)

def generate_matrix():
	"""Generates a random matrix which has a size of random integers between 3 and 10"""
	x = np.random.randint(3, 10)
	y = np.random.randint(3, 10)
	matrix = np.random.rand(x, y)
	rounded_matrix = np.round(matrix, decimals=2)
	return rounded_matrix

def diagonal(input_matrix=generate_matrix()):
	"""
	Creates a new matrix  that is diagonal of the 'input_matrix' and
	a new list that contains values -except 0- of the new matrix
	"""
	try:
		if is_squared(input_matrix):
			matrix_type = np.zeros((len(input_matrix), len(input_matrix[0])))
			list_type = []

			count = 0
			for lis in input_matrix:
				list_type.append(lis[count])
				matrix_type[count][count] = lis[count]
				count+=1

			return list_type, matrix_type
		raise AttributeError("Input matrix is not square matrix")
	except Exception as exception:
		return exception

def upper(input_matrix=generate_matrix()):
	"""Creates a new matrix that is upside of the diagonal of 'input_matrix'"""
	try:
		if is_squared(input_matrix):
			for i in range(len(input_matrix)):
				input_matrix[i][0:i] = 0
			return input_matrix
		raise AttributeError("Input matrix is not square matrix")
	except Exception as exception:
		return exception

def lower(input_matrix=generate_matrix()):
	"""Creates a new matrix that is downside of the diagonal of 'input_matrix'"""
	try:
		if is_squared(input_matrix):
			for i in range(len(input_matrix)-1):
				input_matrix[i][i+1:] = 0
			return input_matrix
		raise AttributeError("Input matrix is not square matrix")
	except Exception as exception:
		return exception

def banded(input_matrix=generate_matrix(), bandwidth=3):
	"""Creates a new matrix only includes the 'bandwidth' diagonal element of the 'input matrix'"""
	try:
		if is_squared(input_matrix):
			new_matrix = np.zeros((len(input_matrix), len(input_matrix)))
			number = (bandwidth-1) / 2
			for i in range(len(input_matrix)):
				for j in range(len(input_matrix)):
					if i+number >= j and i-number <= j:
						new_matrix[i][j] = input_matrix[i][j]
			return new_matrix
		raise AttributeError("Input matrix is not square matrix")
	except Exception as exception:
		return exception

def transpose(input_matrix=generate_matrix()):
	"""Creates a new matrix that is transpose of the 'input_matrix'"""
	try:
		if is_squared(input_matrix):
			new_matrix = np.zeros((len(input_matrix), len(input_matrix)))
			for i in range(len(input_matrix)):
				for j in range(len(input_matrix)):
					new_matrix[i][j] = input_matrix[j][i]
			return new_matrix
		raise AttributeError("Input matrix is not square matrix")
	except Exception as exception:
		return exception