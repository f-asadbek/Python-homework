import matplotlib.pyplot as plt
import numpy as np

# Random x values
x = np.linspace(0, 2/np.pi, 100)

# y functions
y1 = np.sin(x)
y2 = np.cos(x)

# Plot
plt.plot(x, y1, '^:r', label='$sin(x)$')
plt.plot(x, y2, '*-b', label='$cos(x)$')

# Title and labels
plt.title("Sin(x) and Cos(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.show()