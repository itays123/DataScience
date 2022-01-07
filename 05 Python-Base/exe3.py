#Exercise 3 - draw two functions
import matplotlib.pyplot as plt
import numpy as np

# Create grid
ax = plt.gca()
ax.spines['left'].set_position(('axes', 0))
ax.spines['bottom'].set_position(('axes', 0))
plt.grid()

# Create and draw lines
x = np.arange(-20, 21, 1)
y1 = 10 * x + 6
y2 = 2 * (x ** 2) + 2 * x - 100

plt.xlim([np.min(x) - 1,np.max(x) + 1])
plt.ylim([np.min(y1) - 20,np.max(y2) + 20])

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()