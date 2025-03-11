import numpy as np
# Fahrenheit to Celsius
def f_to_c(f):
    return (f - 32) * 5/9

# Vectorizing function
vectorizer = np.vectorize(f_to_c)
a = np.array([32, 68, 100, 212, 77])
print("The result:\n", vectorizer(a))