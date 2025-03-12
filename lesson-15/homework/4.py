import matplotlib.pyplot as plt
import numpy as np

# Random x and y values
np.random.seed(42)  # For reproducibility
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

# Random colors and markers
colors = np.random.rand(100)
markers = np.random.choice(['o', 's', 'D', 'v', '^', '<', '>', 'p', '*', 'h'], 100)

# Scatter plot
plt.figure(figsize=(8, 6))
for i in range(100):
    plt.scatter(x[i], y[i], color=plt.cm.viridis(colors[i]), marker=markers[i], s=50, edgecolors='black')

# Title and labels
plt.title('Scatter Plot of 100 Random Points')
plt.xlabel('X')
plt.ylabel('Y')

# Grid
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
