import numpy as np

x = np.matrix("4,5,16,7; 2,-3,2,3; 3,4,5,6; 4,7,8,9")
print(x)

det_matrix = np.linalg.det(x)
print(det_matrix)