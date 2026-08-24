import numpy as np
A = np.array([[2,3],[1,4]])

# eigenvalues, eigenvector = np.linalg.eig(A)
# print("Eigenvalues:", eigenvalues)
# print("Eigenvectors:", eigenvector)

U,S,V = np.linalg.svd(A)
print("U:",U)
print("S:",S)
print("V:",V)