import matplotlib.pyplot as plt
import numpy as np

# 3D surface
fig = plt.figure()
axis = plt.axes(projection='3d')

# x and y values
x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)

xx, yy = np.meshgrid(x, y)
zz = np.cos(xx ** 2 + yy ** 2)

# plot
surf = axis.plot_surface(xx, yy, zz, cmap='viridis')

# colorbar
fig.colorbar(surf, ax=axis, shrink=0.6, aspect=10)

# title and labels
axis.set_title("$ f(x, y) = \cos(x^2 + y^2) $")
axis.set_xlabel('X')
axis.set_ylabel('Y')
axis.set_zlabel('Z')

plt.show()