import numpy as np

# Coefficients
a = np.array([[4, 5, 6],
              [3, -1, 1],
              [2, 1, -2]])

#Constants
b = np.array([7, 4, 5])

result = np.linalg.solve(a, b)
print("The result:\n", result)