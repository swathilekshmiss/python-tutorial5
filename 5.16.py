import numpy as np
A = np.random.randint(0, 20, (3, 3))
B = np.random.randint(0, 20, (3, 3))
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Addition:\n", A + B)
print("Matrix Multiplication:\n", np.dot(A, B))
print("Transpose of Product Matrix:\n", np.transpose(np.dot(A, B)))