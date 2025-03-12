import matplotlib.pyplot as plt
import numpy as np

# Random x values
x = np.linspace(-10, 10, 1000)

# y function
y = x ** 2 - 4 * x + 4

# Plot
plt.plot(x, y, label = '$f(x) = x^2 - 4x + 4$')

# Title and labels
plt.title('$ f(x) = x^2 - 4x + 4 $')
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.legend()

plt.show()