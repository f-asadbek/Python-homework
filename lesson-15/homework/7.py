import matplotlib.pyplot as plt
import numpy as np

# x and y values
x = np.array(['Product A', 'Product B', 'Product C', 'Product D', 'Product E'])
y = np.array([200, 150, 250, 175, 225])

# colors
colors = np.array(['red', 'blue', 'green', 'black', 'yellow'])

# plot
plt.bar(x, y, color=[i for i in colors], width=0.5, label=[i for i in x])

# title and labels
plt.title('Products')
plt.xlabel('Product names')
plt.ylabel('The sales')
plt.legend()

plt.show()