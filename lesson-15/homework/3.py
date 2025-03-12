import matplotlib.pyplot as plt
import numpy as np

# Random x values
x = np.linspace(-25, 25, 1000)

# for y1 function
y1 = x ** 3
plt.subplot(2, 2, 1)
plt.plot(x, y1, c='g', label='$ f(x) = x^3 $')
plt.title('f(x) = x**3')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# for y2 function
y2 = np.sin(x)
plt.subplot(2, 2, 2)
plt.plot(x, y2, c='b', label='$ f(x) = \sin(x) $')
plt.title('sin(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper left')

# for y3 function
y3 = np.e ** x
plt.subplot(2, 2, 3)
plt.plot(x, y3, c='c', label='$ f(x) = e^x $')
plt.title('e ** x')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# for y4 function
y4 = np.where(x >= -1, np.log(x + 1), np.nan)
plt.subplot(2, 2, 4)
plt.plot(x, y4, c='r', label='$ f(x) = \log(x+1) $ (for $ x \geq 0 $)')
plt.title('log(x + 1)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.show()