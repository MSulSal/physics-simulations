import numpy as np
import matplotlib.pyplot as plt

step = 0.1
x = np.arange(-1, 1 + step, step)
y = np.arange(0, 2 + step, step)
xv , yv = np.meshgrid(x, y, indexing='ij')

plt.scatter(xv, yv, color='gray')
plt.xlim((-1.5, 1.5))
plt.ylim((-0.5, 2.5))
plt.xticks((-1, 0, 1))
plt.yticks((0, 1, 2))
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.axis('square')

plt.show()