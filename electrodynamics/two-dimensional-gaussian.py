import numpy as np
import matplotlib.pyplot as plt

step = 0.05
x, y = np.meshgrid(
    np.arange(-1, 1, step),
    np.arange(-1, 1, step),
    indexing='ij'
)
x0, y0 = 0.3, 0.1
sig = 0.3
g = np.exp(-((x-x0)**2 + (y-y0)**2) / (2 * sig**2))

fig = plt.figure(figsize=(5, 4))
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, g, cmap='gray')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xticks((-1, 0, 1))
ax.set_yticks((-1, 0, 1))
ax.set_zticks((0, 0.5, 1))
ax.view_init(10, -60)
ax.set_rasterized(True)
plt.tight_layout()

plt.show()