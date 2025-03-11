import numpy as np

# The function
def power_func(base, exponent):
    return base ** exponent

# Vectorizing
vectorized_power = np.vectorize(power_func)

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])

print("The output:\n", vectorized_power(bases, exponents))