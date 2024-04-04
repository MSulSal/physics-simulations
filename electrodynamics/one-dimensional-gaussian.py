import matplotlib.pyplot as plt
import numpy as np

step = 0.01
x = np.arange(-1, 1, step)

f = np.exp(-(x - 0.3) ** 2 / (2 * 0.2 ** 2))
g = -np.exp(-(x + 0.3) ** 2 / (2 * 0.3 ** 2))

f_label = r'$+e^{-\frac{(x-0.3)^2}{2 \times 0.2^2}}$'
g_label = r'$-e^{-\frac{(x+0.3)^2}{2 \times 0.3^2}}$'

fig = plt.figure(figsize=(5, 3))
plt.plot(x, f, label=f_label, color='black')
plt.plot(x, g, label=g_label, color='gray')
plt.legend(framealpha=1)
plt.xticks((-1, 0, 1))
plt.yticks((-1, 0, 1))
plt.ylim((-1.2, 1.2))
plt.xlabel('x')
plt.ylabel('y')

plt.show()