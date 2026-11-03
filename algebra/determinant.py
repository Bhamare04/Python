import numpy as np
# A = np.matrix([[1, 2], [3, 4]])
# det_A = np.linalg.det(A)
# print("Determinant of A:", det_A)
# inverse_A = np.linalg.inv(A)
# print("Inverse of A:\n",inverse_A)

#What is block diagonal matrix?
#A block diagonal matrix is a special type of square matrix that is composed of smaller square matrices (blocks) along its diagonal, with all off-diagonal blocks being zero matrices.
#  In other words, a block diagonal matrix has the following structure:
# [ A1  0   0  ...  0 ]
#create a block diagonal matrix using numpy
A1 = np.matrix([[1, 2], [3, 4]])
A2 = np.matrix([[5, 6], [7, 8]])
block_diag_matrix = np.block([[A1, np.zeros((2, 2))], [np.zeros((2, 2)), A2]])
print("Block Diagonal Matrix:\n", block_diag_matrix)

