import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
# Values
x = np.random.normal(0, 1, 1000)

# Histogram
plt.hist(x, color='r', bins=30, edgecolor='black', alpha=0.7)

# Titles and labels
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()