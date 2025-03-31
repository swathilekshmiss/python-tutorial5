import numpy as np 
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
result = A + B
transpose_result = np.transpose(result)
print("Matrix Addition Result:\n", result)
print("Transpose of the Result:\n", transpose_result)