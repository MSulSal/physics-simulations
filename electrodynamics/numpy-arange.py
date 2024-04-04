import numpy as np
import matplotlib.pyplot as plt

# define x and y
step = 0.25
x = np.arange(-1, 1 + step, step)
y = 2 * (x ** 2) + 1

# make a scatter plot with lines that connect adjacent points
plt.scatter(x, y, color='gray')
plt.plot(x, y, color='black')

# make the plot look nice by specifying limits and tick marks
# improve the signal-to-noise ratio of the visualization
plt.xlim((-1.25, 1.25))
plt.ylim((-1, 5))
plt.xticks((-1, 0, 1))
plt.yticks(np.arange(0, 5, 2))
plt.xlabel('x')
plt.ylabel('y')

plt.show()