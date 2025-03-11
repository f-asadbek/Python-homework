import numpy as np

# Coefficients
a = np.array([[10, -2, 3],
              [-2, 8, -1],
              [3, -1, 6]])

#Constants
b = np.array([12, -5, 15])

result = np.linalg.solve(a, b)
print("The result:\n", result)