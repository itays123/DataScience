# Exercise 5 - two-dimentional arrays
import numpy as np

# Create matrix
matrix = np.ones((5, 5))
print(matrix)

maxRowCol = len(matrix) - 1
matrix = matrix * 0
matrix[0] = 1
matrix[maxRowCol] = 1
matrix[:,0] = 1
matrix[:,maxRowCol] = 1
print(matrix)


